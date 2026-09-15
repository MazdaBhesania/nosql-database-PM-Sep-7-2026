# Plan and Implement Azure Cosmos DB for NoSQL

> **Aligned with Microsoft Official Curriculum**: [Plan and implement Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/training/paths/plan-implement-azure-cosmos-db-sql-api/)

Azure Cosmos DB for NoSQL is a fully managed, globally distributed, multi-model NoSQL database service designed for mission-critical applications demanding single-digit millisecond response times and 99.999% availability.

This comprehensive guide covers the three core pillars required to plan, size, configure, and migrate workloads to Azure Cosmos DB.

---

# Module 1: Plan Resource Requirements

Successful Cosmos DB deployments begin with workload evaluation and capacity modeling. Unlike traditional databases sized by CPU cores and RAM, Cosmos DB abstracts compute and memory into a normalized currency called **Request Units (RU/s)**.

---

## 1.1 Understanding Request Units (RU/s)

A **Request Unit (RU)** is a rate-based currency that abstracts the physical resources (CPU, memory, disk IOPS) required to execute database operations.

```text
1 RU = The cost to perform a point read (fetch by id and partition key)
       of a single 1 KB item.
```

### RU Consumption Factors
| Factor | Impact on RU Cost |
| :--- | :--- |
| **Item Size** | Larger items consume more RUs. Reading a 2 KB item costs ~2 RUs; 10 KB costs ~10 RUs. |
| **Operation Type** | **Point Reads** (using `id` + `partitionKey`) are cheapest (1 RU).<br>**Writes/Inserts** cost ~5–7x more than reads because of data replication across 4 local replicas and synchronous index updates.<br>**Deletes** cost ~2–3 RUs. |
| **Query Complexity** | Queries involving `JOIN`, aggregations (`SUM`, `AVG`), regular expressions, or scans consume significantly more RUs than point reads. |
| **Partition Scope** | **Single-partition queries** route directly to one physical partition (efficient).<br>**Cross-partition queries** fan out to all physical partitions (high RU cost and latency). |
| **Indexing Policy** | Indexing all fields increases write RU cost. Excluding high-frequency write fields reduces RU overhead. |
| **Consistency Level** | Strong and Bounded Staleness reads consume ~2x the RUs of Session or Eventual reads. |

### Formula for Throughput Estimation
$$\text{Total Required RU/s} = (\text{Peak Reads/sec} \times \text{RU per Read}) + (\text{Peak Writes/sec} \times \text{RU per Write})$$

*Example*: If an application performs 500 point reads/sec (1 RU each) and 100 inserts/sec of 1 KB items (5 RUs each):
$$\text{Total RU/s} = (500 \times 1) + (100 \times 5) = 500 + 500 = 1,000 \text{ RU/s}$$

---

## 1.2 The Five Consistency Levels

Traditional databases force a binary choice between ACID transactions (strong consistency) and eventual consistency (BASE). Azure Cosmos DB offers **five mathematically well-defined consistency levels** along a continuous spectrum:

```text
[ Strong ] ──► [ Bounded Staleness ] ──► [ Session ] ──► [ Consistent Prefix ] ──► [ Eventual ]
<────── Highest Consistency ───────                  ─────── Lowest Latency / ──────►
<────── Lowest Throughput (2x RU) ─                  ─────── Highest Throughput (1x) ─►
```

### Detailed Consistency Comparison
| Consistency Level | Guarantee | Trade-Offs | Ideal Use Case |
| :--- | :--- | :--- | :--- |
| **Strong** | Linearizable reads. Guarantees that reads always return the latest committed version. Synchronously writes across all replica regions. | Highest latency; reads cost 2x RUs; limited to regions < 8000 km apart. Not available with multi-region writes. | Financial transactions, inventory reservation, banking ledgers. |
| **Bounded Staleness** | Reads lag behind writes by at most an explicit threshold: **$K$ versions** (updates) or **$T$ time interval** (5s to 1 day). | Deterministic staleness window; reads cost 2x RUs; higher read latency than Session. | Real-time dashboards, package tracking, sports scoreboards. |
| **Session** *(Default)* | **Monotonic reads, monotonic writes, read-your-own-writes**. Guarantees consistency within an application session token. | Single-region latency, lowest cost (1x RU); cross-session reads may see brief replication delay. | User profiles, social media feeds, e-commerce shopping carts. (Covers 85%+ of apps). |
| **Consistent Prefix** | Reads never see out-of-order writes. If updates occur in order $A \rightarrow B \rightarrow C$, a reader sees $A$, then $A, B$, never $B$ before $A$. | Low latency, 1x RU cost; does not guarantee how fresh data is. | Activity logs, messaging comment threads, status updates. |
| **Eventual** | Weakest consistency. No order guarantee; replicas eventually converge when writes cease. | Lowest latency, highest throughput, 1x RU cost. | Aggregated analytics, video view counters, customer ratings. |

---

## 1.3 High Availability & Multi-Region Distribution

Azure Cosmos DB replicates data natively at two layers:
1. **Intra-region**: 4 local replicas per physical partition (1 Primary, 3 Secondary followers).
2. **Inter-region**: Global replication across chosen Azure regions.

```text
                           [ Global Client Traffic ]
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
┌───────────────────────┐                           ┌───────────────────────┐
│  East US (Region 1)   │ ◄── Active-Active Sync ──►│  West US (Region 2)   │
│                       │                           │                       │
│  [Primary Write]      │                           │  [Active Write]       │
│  [Local Replicas: 4]  │                           │  [Local Replicas: 4]  │
└───────────────────────┘                           └───────────────────────┘
```

### Configuration Options
- **Single-Region Write with Multi-Region Read**:
  - One region handles all writes; other regions serve read traffic locally.
  - Failover: Automatic or manual failover prioritization list.
  - SLA: 99.99% availability for reads and writes.
- **Multi-Region Writes (Active-Active)**:
  - All distributed regions accept both reads and writes.
  - Lowest write latencies globally (< 10 ms at 99th percentile).
  - SLA: **99.999%** availability for both reads and writes.

### Conflict Resolution in Multi-Region Writes
When two clients write simultaneously to different regions with the same `id` and `partitionKey`, Cosmos DB resolves conflicts using:
1. **Last-Write-Wins (LWW) (Default)**: Uses an internally maintained timestamp property (`_ts`) or a user-defined numeric property (e.g., `/userTimestamp`). The highest value wins.
2. **Custom Merge Procedure**: A user-defined JavaScript stored procedure executes conflict-resolution logic on conflict feeds.

---

# Module 2: Configure Azure Cosmos DB for NoSQL

Once capacity and consistency requirements are planned, you must configure throughput offerings, partitioning boundaries, indexing policies, and data lifecycles.

---

## 2.1 Throughput Offerings: Manual vs. Autoscale vs. Serverless

Cosmos DB offers three throughput models:

```text
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     Manual Provisioned  │   Autoscale Provisioned │       Serverless        │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Fixed RU/s (e.g. 1000)  │ Automatically scales    │ Pure pay-per-request    │
│ Billed per hour for     │ between 10% and 100%    │ Billed only for RUs and │
│ provisioned amount      │ of Max RU/s             │ storage consumed        │
│ Predictable workloads   │ Spiky/variable traffic  │ Dev/Test, low traffic   │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### 1. Manual Provisioned Throughput
- You specify a static RU/s (minimum 400 RU/s, increments of 100 RU/s).
- Best when traffic is steady and predictable 24/7.
- If traffic exceeds provisioned RU/s, Cosmos DB returns HTTP status **429 (Too Many Requests)**.

### 2. Autoscale Provisioned Throughput
- You set a **Max RU/s** ($T_{max}$, minimum 1,000 RU/s).
- The system instantaneously scales between $0.1 \times T_{max}$ and $T_{max}$ based on incoming load.
- *Example*: Setting Max RU/s = 4,000 means the system scales dynamically from 400 to 4,000 RU/s. During idle periods, you only pay for 400 RU/s.

### 3. Serverless
- No provisioning required. Charges apply strictly to RUs consumed per request.
- Maximum container storage: 1 TB.
- Maximum burst throughput: 5,000 RU/s.
- Ideal for dev/test environments, prototypes, or background jobs with long dormant periods.

---

## 2.2 Container vs. Database Throughput

You can provision throughput at two distinct resource levels:

```text
             DATABASE (Shared Throughput)
             ┌────────────────────────────────────────────────┐
             │ Allocated: 1,000 RU/s                          │
             │   ├── Orders Container (shares pool)           │
             │   ├── Products Container (shares pool)         │
             │   └── Customers Container (shares pool)        │
             └────────────────────────────────────────────────┘

             DEDICATED CONTAINER THROUGHPUT
             ┌────────────────────────────────────────────────┐
             │ Orders Container: 5,000 RU/s (Guaranteed)      │
             └────────────────────────────────────────────────┘
```

| Dimension | Dedicated Container Throughput | Shared Database Throughput |
| :--- | :--- | :--- |
| **Throughput Guarantee** | Guaranteed exclusively to that specific container. No "noisy neighbor" effect. | Shared among all containers in the database. |
| **Minimum RU/s** | 400 RU/s per container. | 400 RU/s for the entire database. |
| **Cost Profile** | Higher if you have dozens of low-traffic collections ($N \times 400 \text{ RU/s}$). | Cost-effective for multiple low-traffic containers sharing a single RU pool. |
| **When to use** | High-throughput tables, mission-critical core entities. | Multi-tenant microservices, small auxiliary lookup collections. |

---

## 2.3 Time to Live (TTL) Configuration

Time to Live (TTL) provides automatic deletion of items from a container after a predefined period. Cosmos DB cleans up expired documents in the background without impacting provisioned RU/s or client performance.

### Configuration Hierarchy
1. **Container-level `DefaultTimeToLive`**:
   - `Off` (null): Items never expire automatically (default).
   - `On (no default)` (`-1`): TTL is active, but items will only expire if they explicitly contain an item-level `ttl` property.
   - `On (with default)` (positive integer $N$): Items expire after $N$ seconds unless overridden.
2. **Item-level `ttl` property**:
   - Overrides container default.
   - Example item:
     ```json
     {
       "id": "cart-session-881",
       "userId": "usr-102",
       "ttl": 3600,
       "items": ["prod-1", "prod-2"]
     }
     ```
     *This specific document will automatically be deleted 3,600 seconds (1 hour) after its last update.*

---

## 2.4 Indexing Policies

By default, Azure Cosmos DB automatically indexes **every property of every item** using an inverted index. While this allows arbitrary ad-hoc queries, it increases write RU costs and index storage.

### Indexing Modes
- **Consistent**: Indexes are updated synchronously with every write/update. Queries are immediately consistent with writes.
- **None**: Indexing is disabled. Writes consume minimum possible RUs, but queries require full table scans.

### Custom Indexing Policy Example
```json
{
  "indexingMode": "consistent",
  "automatic": true,
  "includedPaths": [
    {
      "path": "/*"
    }
  ],
  "excludedPaths": [
    {
      "path": "/largeDescription/*"
    },
    {
      "path": "/\"_etag\"/?"
    }
  ],
  "compositeIndexes": [
    [
      { "path": "/category", "order": "ascending" },
      { "path": "/price", "order": "descending" }
    ]
  ]
}
```

### Composite Indexes
Required whenever a single query has:
1. An `ORDER BY` clause with two or more properties (e.g., `ORDER BY c.category ASC, c.price DESC`).
2. A filter on multiple properties combined with an `ORDER BY` clause.

---

# Module 3: Move Data Into and Out of Azure Cosmos DB for NoSQL

Migrating data into Azure Cosmos DB requires choosing between offline and online migration patterns and selecting the right tooling.

---

## 3.1 Migration Strategies: Offline vs. Online

```text
Offline (Batch / Cold Cutover)          Online (Zero-Downtime Live Sync)
-----------------------------          --------------------------------
1. Stop writes to source db            1. Perform initial historical snapshot load
2. Export data                         2. Stream ongoing changes (Change Data Capture)
3. Bulk load into Cosmos DB            3. Verify replica catch-up
4. Switch application connection       4. Instant cutover with near-zero downtime
```

| Strategy | Advantages | Trade-Offs |
| :--- | :--- | :--- |
| **Offline** | Simple setup, no dual-write synchronization needed, predictable. | Requires scheduled maintenance window and application downtime. |
| **Online** | Zero or near-zero application downtime, zero user disruption. | More complex setup; requires CDC (Change Data Capture) pipeline. |

---

## 3.2 Enterprise Migration Tools

### 1. Azure Data Factory (ADF)
- Cloud-based enterprise ETL/ELT service.
- Features native Azure Cosmos DB connectors (both Source and Sink).
- Supports parallel bulk ingestion, automatic type conversion, and scalable integration runtimes.
- Best for enterprise-scale migrations (> 100 GB) or multi-source data warehouses.

### 2. Azure Cosmos DB Desktop Data Migration Tool (Open Source)
- Cross-platform CLI and GUI application maintained by Microsoft.
- Direct migrations from:
  - JSON files
  - CSV / TSV files
  - MongoDB
  - SQL Server / Azure SQL
  - Amazon DynamoDB
- Ideal for small to medium migrations (< 50 GB) and quick developer imports.

### 3. Apache Spark / Azure Synapse Link
- High-throughput parallel migration for big data pipelines.
- Reads source partitions in parallel and writes via Cosmos DB Spark 3.x connector using the bulk execution engine.

---

## 3.3 Best Practices for Ingestion Optimization

When performing large-scale bulk migrations:
1. **Temporarily Scale Up RU/s**: Before starting migration, scale throughput up (e.g., to 20,000+ RU/s) or switch to autoscale. Scale back down to baseline after ingestion completes.
2. **Pre-Split Partitions**: If loading > 100 GB, pre-create physical partitions by provisioning high RU/s (e.g., 10,000 RU/s creates multiple physical partitions) so data distributes evenly.
3. **Temporarily Disable Indexing**: Set `indexingMode: "none"` on target container during initial mass ingestion. Re-enable to `"consistent"` after migration is complete.
4. **Distribute Partition Keys**: Avoid bulk-loading data sequentially sorted by the partition key to prevent creating a "hot physical partition".
5. **Use SDK Bulk Mode**:
   ```csharp
   CosmosClientOptions options = new CosmosClientOptions()
   {
       AllowBulkExecution = true
   };
   CosmosClient client = new CosmosClient(endpoint, key, options);
   ```
   Bulk execution groups individual write operations into micro-batches, maximizing throughput and reducing network round-trips by up to 80%.
