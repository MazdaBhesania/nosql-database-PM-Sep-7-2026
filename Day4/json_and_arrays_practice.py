# Python JSON & Arrays Practice Lab

# -------------------------------------------------------------
# Exercise 1: Create a Document (Dictionary)
# -------------------------------------------------------------
# Create a dictionary named student with:
# name = "Sarah"
# age = 25
# course = "NoSQL"

student = {
    # Write your code here
}

print("Student:", student)


# -------------------------------------------------------------
# Exercise 2: Read Values from a Document
# -------------------------------------------------------------
employee = {
    "id": 101,
    "name": "John Doe",
    "department": "IT",
    "salary": 75000
}

# Get the name and salary of the employee:
emp_name = employee["name"]
emp_salary = employee["salary"]

print("Employee Name:", emp_name)
print("Employee Salary:", emp_salary)


# -------------------------------------------------------------
# Exercise 3: Update and Add New Fields
# -------------------------------------------------------------
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

# 1. Update year to 2024
# 2. Add color = "Blue"

# Write your code here:


print("Updated Car:", car)


# -------------------------------------------------------------
# Exercise 4: Nested Documents (Object inside Object)
# -------------------------------------------------------------
user = {
    "username": "alex99",
    "profile": {
        "city": "Toronto",
        "country": "Canada"
    }
}

# 1. Print the user's city
# 2. Change city to "Montreal"

# Write your code here:


print("Updated User:", user)


# -------------------------------------------------------------
# Exercise 5: JSON Arrays (Lists)
# -------------------------------------------------------------
# In Python, an array is written with square brackets []
skills = ["Python", "MongoDB", "CosmosDB", "SQL"]

# 1. Print the first skill (index 0)
# 2. Print the second skill (index 1)

# Write your code here:



# -------------------------------------------------------------
# Exercise 6: Document with an Array
# -------------------------------------------------------------
product = {
    "id": "P100",
    "title": "Headphones",
    "price": 150,
    "tags": ["audio", "wireless", "electronics"]
}

# 1. Print product title
# 2. Print the first tag ("audio")

# Write your code here:



# -------------------------------------------------------------
# Exercise 7: Array of Documents (Simulating Database Results)
# -------------------------------------------------------------
# A list containing 3 documents
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 95}
]

# 1. Print the name of the first student (index 0)
# 2. Print the score of the third student (index 2)

# Write your code here:


