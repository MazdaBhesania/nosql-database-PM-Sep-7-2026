# Day 4: Python Crash Course for NoSQL (The 30-Minute Foundation)

> **Instructor & Student Guide**: If students have never written code before, teach **only these 5 concepts**. This is 100% of the Python required to understand and write NoSQL SDK code. Nothing more, nothing less.

---

## Concept 1: Variables (Labeled Boxes)

A variable is just a labeled box that holds a piece of information so we can reuse it later.

```python
student_name = "Sarah Connor"   # Text (String) - always in quotes
student_age = 28                 # Number (Integer) - no quotes
course_fee = 499.50              # Decimal number (Float)
is_enrolled = True               # True or False (Boolean) - Capital T or F!
```

### Whiteboard Analogy for Students:
> *"Think of a variable like writing a label on a cardboard box. Instead of retyping `'https://myaccount.documents.azure.com:443/'` ten times, we put it in a box named `ENDPOINT`."*

```python
ENDPOINT = "https://myaccount.documents.azure.com:443/"
```

---

## Concept 2: The JSON Bridge (Dictionaries & Lists)

This is the most important concept in NoSQL programming. **If they understand JSON, they already know 80% of Python!**

### 1. Dictionary = JSON Object `{}`
In Python, curly braces `{}` create a **Dictionary** (`dict`). It stores `key: value` pairs.

```python
# A document in Python is just a dictionary:
patient = {
    "id": "PAT-101",
    "name": "Bruce Wayne",
    "city": "Gotham"
}

# How to GET a value out of the box:
print(patient["name"])  # Prints: Bruce Wayne

# How to ADD or UPDATE a value:
patient["city"] = "Toronto"    # Updates city
patient["bloodType"] = "O+"     # Adds new field
```

### 2. List = JSON Array `[]`
Square brackets `[]` create a **List** (`list`).

```python
hobbies = ["Reading", "Gaming", "Swimming"]

# Python counts starting at ZERO (0):
print(hobbies[0])  # Prints: Reading
print(hobbies[1])  # Prints: Gaming
```

### Combining Both (Just like Day 1 JSON!):
```python
order = {
    "orderId": "ORD-01",
    "total": 150.00,
    "items": ["Headphones", "USB Cable"]  # List inside a Dictionary!
}
```

---

## Concept 3: What Does `import` Mean? (The App Store Analogy)

Python comes with a few basic tools out of the box. But Python doesn't know how to talk to Azure Cosmos DB or MongoDB by default.

To give Python new powers, we install an external "app" (library) and **import** it.

```text
Step 1: Install the app (Terminal):      pip install azure-cosmos
Step 2: Open the app in your code:       from azure.cosmos import CosmosClient
```

### Whiteboard Analogy for Students:
> *"Think of Python like a brand-new smartphone. If you want to use Instagram or WhatsApp, you download it from the App Store (`pip install`), and then you tap on the app to open it (`import`)."*

---

## Concept 4: The Dot (`.`) Means "Do an Action" (Methods)

Students get confused when they see:
```python
container.read_item(...)
client.get_database_client(...)
```

Explain the **Dot (`.`)** using the **Remote Control Analogy**:

```text
Object . Action(Details)
  │        │       │
TV_Remote.turn_on(channel=5)
container.read_item(item="STU-01", partition_key="STU-01")
```

* `container` is the object (the box representing our Cosmos container).
* The dot `.` means **"hey, do this action for me"**.
* `read_item(...)` is the action (method) we are asking it to do.
* The items inside the parentheses `(...)` are the specific details it needs to do the job.

---

## Concept 5: The `for` Loop (Going Through a List One-by-One)

When we query a database, the database returns a **list of documents**. How do we look at them? With a `for` loop.

```python
students = [
    {"name": "Alice", "grade": 95},
    {"name": "Bob", "grade": 88},
    {"name": "Charlie", "grade": 92}
]

# Read this aloud as: "For each student in our students list, do this:"
for student in students:
    print(student["name"], "scored", student["grade"])
```

### Output:
```text
Alice scored 95
Bob scored 88
Charlie scored 92
```

---

## 🎓 The "Put It All Together" Translation Chart

Show students how their database concepts translate directly into Python SDK code:

| What you do in Azure Portal | What it looks like in Python |
| :--- | :--- |
| **Open Azure Portal** | `client = CosmosClient(ENDPOINT, KEY)` |
| **Click Database "CollegeDB"** | `db = client.get_database_client("CollegeDB")` |
| **Click Container "Students"** | `container = db.get_container_client("Students")` |
| **Click "New Item" & paste JSON** | `container.upsert_item({"id": "1", "name": "Dipen"})` |
| **Look up item by ID** | `item = container.read_item(item="1", partition_key="1")` |
| **Click "Execute Query"** | `for item in container.query_items(query="SELECT * FROM c"):` |

---

## ⏱️ Suggested 25-Minute Classroom Delivery Plan

| Time | Topic | Activity |
| :--- | :--- | :--- |
| **00 - 05 min** | Variables | Write 3 variables on board: name, age, isStudent. Have 2 students give their own. |
| **05 - 12 min** | Dictionaries = JSON | Show a JSON document from Day 1. Show the Python dictionary. Point out they are 99% identical! |
| **12 - 17 min** | The Dot `.` Notation | Remote control analogy: `object.action()`. |
| **17 - 22 min** | Import / Pip | App Store analogy: `pip install` = download app; `import` = open app. |
| **22 - 25 min** | Live Demo | Open [`starter_python_sdk.py`](file:///Users/dipenparihar/Documents/CBC/DSAI/NoSQL/Day4/starter_python_sdk.py) and run it together! |
