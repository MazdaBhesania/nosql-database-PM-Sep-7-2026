# Day 3: MongoDB Knowledge & Azure Cosmos DB Plan and Implement

Welcome to **Day 3** of the NoSQL Database course! 

In Day 1, we covered the basics of NoSQL data models, XML vs. JSON formats, and local MongoDB setup. In Day 2, we explored Azure Cosmos DB's core architecture, resource hierarchy, and how it compares to traditional SQL Server databases.

Today, in **Day 3**, we take a deep dive into two critical areas:
1. **Core MongoDB Practical Knowledge**: Deepening your document database mastery with BSON internals, CRUD operations, query operators, projection, indexing, and the powerful Aggregation Framework.
2. **Plan and Implement Azure Cosmos DB for NoSQL**: Fully aligned with Microsoft's official curriculum ([Plan and implement Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/training/paths/plan-implement-azure-cosmos-db-sql-api/)), covering capacity planning, Request Units (RU/s), consistency levels, throughput offerings, indexing policies, and enterprise data migration.

---

## 📚 Learning Modules & Table of Contents

| Resource | Description |
| :--- | :--- |
| **[1. MongoDB Knowledge Guide](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day3/mongodb_knowledge.md)** | Comprehensive guide on MongoDB concepts, JSON vs BSON, shell commands (`mongosh`), CRUD operators, indexing, and Aggregation Pipeline stages. |
| **[2. Azure Cosmos DB: Plan and Implement](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day3/cosmos_db_plan_and_implement.md)** | Microsoft Learn-aligned guide covering: <br>• **Module 1**: Plan Resource Requirements (RU/s, 5 Consistency Levels, Multi-region HA)<br>• **Module 2**: Configure Cosmos DB (Manual vs Autoscale vs Serverless, Database vs Container throughput, TTL, Indexing Policies)<br>• **Module 3**: Move Data Into & Out of Cosmos DB (Azure Data Factory, Desktop Data Migration Tool, Bulk mode) |
| **[3. Hands-On Labs & Certification Questions](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day3/labs_and_exercises.md)** | Practical step-by-step exercises with solutions for MongoDB and Cosmos DB, scenario-based capacity calculation labs, and 10 certification-style quiz questions with explanations. |
| **[4. MongoDB Lab (Student Edition - No Answers)](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day3/mongodb_lab.md)** | Practice lab sheet with 17 realistic query, update, aggregation, and indexing challenges designed for students to solve without answers. |
| **[5. Sample Dataset (`sample_data.json`)](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day3/sample_data.json)** | Clean, realistic e-commerce and retail sample dataset formatted for easy import into MongoDB Compass, `mongosh`, or Azure Cosmos DB Data Explorer. |

---

## 🎯 Learning Objectives

By the end of Day 3, you will be able to:
1. **Model and Query Documents in MongoDB**:
   - Understand the difference between JSON and binary BSON serialization.
   - Perform expressive CRUD queries using comparison, logical, element, and array operators.
   - Construct multi-stage Aggregation Pipelines (`$match`, `$group`, `$project`, `$unwind`, `$sort`).
   - Create single, compound, and multikey indexes to optimize query performance.
2. **Plan Cosmos DB Workload Resources**:
   - Calculate Request Units (RU/s) based on item size, read/write ratios, and concurrency.
   - Select the optimal consistency level (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual) based on latency vs. consistency trade-offs.
   - Design for High Availability and disaster recovery with multi-region reads and multi-region writes.
3. **Configure Throughput, TTL, and Indexing**:
   - Decide between Serverless, Standard Provisioned, and Autoscale throughput.
   - Choose between dedicated container throughput and shared database throughput.
   - Configure Time to Live (TTL) at container and document levels for automated data lifecycles.
   - Customize Cosmos DB indexing policies with included paths, excluded paths, and composite indexes.
4. **Execute Enterprise Data Migration**:
   - Formulate offline vs. online migration strategies.
   - Migrate data seamlessly into Azure Cosmos DB using Azure Data Factory and the open-source Desktop Data Migration Tool.
