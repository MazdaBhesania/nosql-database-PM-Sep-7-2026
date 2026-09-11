# Azure Cosmos DB Basics

## What is Azure Cosmos DB?

Azure Cosmos DB is Microsoft's globally distributed NoSQL database service.

Unlike SQL Server, Cosmos DB stores data as JSON documents and is designed to scale automatically across multiple regions.

---

# Cosmos DB Resource Hierarchy

```text
Cosmos DB Account
    └── Database
            └── Container
                    └── Item (Document)
```

Example:

```text
studentmm (Cosmos DB Account)
    └── CollegeDB (Database)
            └── Students (Container)
                    └── {"id":"1","name":"Dipen"}
```

---

# What is a Cosmos DB Account?

A Cosmos DB Account is the top-level Azure resource.

It contains:

- Databases
- Containers
- Connection endpoint
- Security keys
- Replication settings
- Region configuration

Example:

```text
Account Name: studentmm
Endpoint: https://studentmm.documents.azure.com
```

Think of the account as the SQL Server instance in SQL Server.

---

# Is a Cosmos DB Account Required?

Yes.

You must create a Cosmos DB Account before creating:

- Databases
- Containers
- Documents

Without an account, nothing else can be created.

---

# SQL Server vs Cosmos DB

| SQL Server | Cosmos DB |
|------------|-----------|
| SQL Server Instance | Cosmos DB Account |
| Database | Database |
| Table | Container |
| Row | Item (Document) |
| Primary Key | id + Partition Key |

---

# Why Does Cosmos DB Use Containers Instead of Tables?

In SQL Server:

```sql
CREATE TABLE Students
(
    StudentID INT,
    Name VARCHAR(50)
)
```

All rows must follow the same schema.

Example:

| StudentID | Name |
|------------|------|
| 1 | Dipen |
| 2 | John |

---

In Cosmos DB, data is stored as JSON documents.

Document 1:

```json
{
    "id": "1",
    "name": "Dipen"
}
```

Document 2:

```json
{
    "id": "2",
    "name": "John",
    "course": "Cloud Computing"
}
```

Notice that the second document has an extra field.

Because documents can have different structures, Cosmos DB uses the term **Container** instead of **Table**.

---

# What is a Container?

A Container is where Cosmos DB stores documents.

A Container handles:

- Data storage
- Partitioning
- Scalability
- Performance (RU/s)

Example:

```text
CollegeDB
    └── Students
```

Here, Students is a container.

---

# What is an Item?

An Item is a JSON document stored inside a container.

Example:

```json
{
    "id": "STU001",
    "name": "Dipen",
    "program": "Cloud Computing"
}
```

Items are equivalent to rows in SQL Server.

---

# Creating an Item Through Azure Portal

1. Open Azure Portal.
2. Open Cosmos DB Account.
3. Click Data Explorer.
4. Expand Database.
5. Expand Container.
6. Click New Item.
7. Enter JSON.

Example:

```json
{
    "id": "1",
    "name": "Dipen",
    "course": "Cloud Computing"
}
```

8. Click Save.

---

# Example Student Database Structure

```text
CollegeDB
│
├── Students
├── Courses
├── Instructors
└── Enrollments
```

Each container stores JSON documents related to that entity.

---

# Key Points

- Cosmos DB Account = SQL Server Instance
- Database = Database
- Container ≈ Table
- Item ≈ Row
- Data is stored as JSON documents
- Documents can have different structures
- Containers are used because Cosmos DB is schema-flexible and highly scalable