# MongoDB Hands-On Lab: Student Edition (Exercises)

**Instructions**: Complete the following tasks using `mongosh` or MongoDB Compass. Use the provided dataset [`sample_data.json`](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day3/sample_data.json). Write down your MongoDB query/command under each task.

---

## Lab Setup: Import Data

Before beginning the exercises, ensure MongoDB is running and import the sample dataset into a database called `store_db` and a collection called `products`.

### Option A: Using Terminal (`mongoimport`)
```bash
mongoimport --db store_db --collection products --file sample_data.json --jsonArray --drop
```

### Option B: Using `mongosh`
```javascript
use store_db
db.products.drop() // clear previous data if needed

// In mongosh, load and insert:
const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./sample_data.json', 'utf8'));
db.products.insertMany(data);
```

### Verification
Run the following command to verify that 8 documents were loaded:
```javascript
db.products.countDocuments()
```

---

## Part 1: Basic & Comparison Queries

### Task 1.1: Exact Match
Find all products where the `category` is `"Electronics"`.

```javascript
// Write your query here:

```

---

### Task 1.2: Range Filter
Find all products with a `price` greater than or equal to `$100` and less than or equal to `$300`.

```javascript
// Write your query here:

```

---

### Task 1.3: In-List Filter (`$in`)
Find all products whose `category` is either `"Audio"` or `"Furniture"`.

```javascript
// Write your query here:

```

---

### Task 1.4: High Rating & In-Stock
Find all products that have a `rating` greater than or equal to `4.7` AND a `stock` of at least `20` units.

```javascript
// Write your query here:

```

---

## Part 2: Projections, Sorting & Pagination

### Task 2.1: Projection
Find all products in the `"Electronics"` category, but display **only** the `name`, `price`, and `sku` fields. Suppress the default `_id` field from the output.

```javascript
// Write your query here:

```

---

### Task 2.2: Sorting
List all products sorted by `price` from highest to lowest (descending order).

```javascript
// Write your query here:

```

---

### Task 2.3: Pagination (`skip` & `limit`)
Retrieve the top 3 most expensive products after skipping the first single most expensive product (i.e. rank 2, 3, and 4 by price).

```javascript
// Write your query here:

```

---

## Part 3: Querying Nested Objects & Arrays

### Task 3.1: Nested Field Filter
Query products where the nested field `specifications.batteryLifeHours` is greater than or equal to `30`.

```javascript
// Write your query here:

```

---

### Task 3.2: Array Element Match
Find all products that have `"bluetooth"` included in their `tags` array.

```javascript
// Write your query here:

```

---

### Task 3.3: Multiple Array Elements Match (`$all`)
Find all products whose `tags` array contains **both** `"wireless"` AND `"office"`.

```javascript
// Write your query here:

```

---

### Task 3.4: Array Length Filter (`$size`)
Find all products that have exactly `3` tags in their `tags` array.

```javascript
// Write your query here:

```

---

## Part 4: Update Operations

### Task 4.1: Update a Single Field (`$set`)
Update the product with SKU `"TECH-KB-01"`. Set its `isFeatured` status to `false` and update its `rating` to `4.9`.

```javascript
// Write your query here:

```

---

### Task 4.2: Increment a Numeric Value (`$inc`)
The store received a restock. Increase the `stock` count of the product with SKU `"TECH-MS-02"` by `25` units.

```javascript
// Write your query here:

```

---

### Task 4.3: Multiply a Field (`$mul`)
Apply a 5% inflation price increase to all products in the `"Furniture"` category.

```javascript
// Write your query here:

```

---

### Task 4.4: Add Element to Array Without Duplicates (`$addToSet`)
Add the tag `"ergonomic"` to the product with SKU `"TECH-KB-01"`. Ensure the tag is not duplicated if it already exists.

```javascript
// Write your query here:

```

---

### Task 4.5: Remove an Element from an Array (`$pull`)
Remove the tag `"wired"` from the `tags` array of the product with SKU `"TECH-KB-01"`.

```javascript
// Write your query here:

```

---

### Task 4.6: Upsert Operation
Attempt to update a product with SKU `"TECH-CAM-01"`. If it does not exist, insert it with the following fields:
- `name`: `"4K Ultra HD Webcam"`
- `category`: `"Electronics"`
- `price`: `89.99`
- `stock`: `50`

```javascript
// Write your query here:

```

---

## Part 5: Delete Operations

### Task 5.1: Delete a Single Document
Delete the product that has SKU `"TECH-HB-04"`.

```javascript
// Write your query here:

```

---

### Task 5.2: Delete Multiple Documents
Delete all products that have a `stock` of `0` or less.

```javascript
// Write your query here:

```

---

## Part 6: Aggregation Framework Challenges

### Challenge 6.1: Category Summary Metrics
Write an aggregation pipeline that:
1. Groups all products by `category`.
2. Calculates:
   - `totalProducts`: count of products in each category.
   - `avgPrice`: average price of products in each category (round to 2 decimal places).
   - `totalStock`: total sum of items in stock.
3. Sorts the output by `totalStock` in descending order.

```javascript
// Write your aggregation pipeline here:

```

---

### Challenge 6.2: High-Value Inventory by Category
Write an aggregation pipeline that:
1. Filters for products that have a `rating` greater than or equal to `4.5`.
2. Groups by `category`.
3. Calculates `totalInventoryValue` (the sum of `price * stock` for each product).
4. Displays only categories where `totalInventoryValue` is greater than `$5,000`.

```javascript
// Write your aggregation pipeline here:

```

---

### Challenge 6.3: Unwinding Tags
Write an aggregation pipeline that:
1. Deconstructs (unwinds) the `tags` array so each tag is its own document.
2. Groups by `tag`.
3. Counts how many products are associated with each tag (`tagCount`).
4. Sorts by `tagCount` in descending order.
5. Returns only the top 5 most popular tags.

```javascript
// Write your aggregation pipeline here:

```

---

## Part 7: Indexing & Performance Optimization

### Task 7.1: Single Field Index
Create an ascending index on the `category` field.

```javascript
// Write your command here:

```

---

### Task 7.2: Compound Index
Create a compound index on `category` (ascending) and `price` (descending).

```javascript
// Write your command here:

```

---

### Task 7.3: Explain Query Execution
Use `.explain("executionStats")` to verify whether the following query utilizes your compound index:

```javascript
db.products.find({ category: "Electronics" }).sort({ price: -1 })
```

What stage is shown under `winningPlan.inputStage` or `winningPlan.stage`? (`COLLSCAN` or `IXSCAN`?)

```text
// Your observation:

```
