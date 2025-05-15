# **Lesson 08 — Advanced SQL and Database Integration**

## **Lesson Overview**
**Learning objective:** Students will deepen their understanding of SQL by learning advanced techniques such as subqueries, complex `JOIN`s, aggregation with functions, and using `HAVING` for conditional filtering. This lesson also introduces performance optimization techniques, transactions, parameterized queries, window functions, and more.

**Topics:**
1. Subqueries: Embedding queries within other SQL statements for dynamic filtering or calculations.
2. Complex JOINs: Using INNER and LEFT JOINs across multiple related tables.
3. Aggregation Functions: Using `MIN()`, `MAX()`, `AVG()`, `COUNT()` with `GROUP BY`.
4. Aggregation with HAVING: Filtering grouped results using `HAVING` after aggregation.
5. Performance Optimization: Creating indexes to speed up frequent queries.
6. Transactions and Rollbacks: Ensuring consistency with `BEGIN`, `COMMIT`, and `ROLLBACK`.
7. Parameterized Queries: Preventing SQL injection using safe input handling with placeholders.
8. Window Functions: Applying `RANK()`, `ROW_NUMBER()`, and `OVER()` for row-level analytics.
9. Date and Time Functions: Calculating durations and extracting date components using `JULIANDAY()` and related functions.
10. Python Integration: Writing and executing SQL queries within Python scripts using `sqlite3`.

---

## **8.1 Understanding Subqueries**

### **Overview**
Subqueries are nested SQL queries used to perform intermediate calculations or selections before the main query executes.

### **Key Concepts:**
- Use subqueries to fetch results dynamically within another query.
- Common use cases include finding maximum, minimum, or aggregated values.

### **Example:**
Find the highest-paid employee in each department using a subquery.
```sql
SELECT department_id, employee_id, salary
FROM Employees AS e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department_id = e.department_id
);
```

### **Implementation in Python:**
```python
# Example using SQLite
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Execute the query
query = """
SELECT department_id, employee_id, salary
FROM Employees AS e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department_id = e.department_id
);
"""
cursor.execute(query)
print(cursor.fetchall())

conn.close()
```

---

## **8.2 Complex JOINs**

### **Overview**
Complex `JOIN`s allow you to retrieve data from multiple related tables.

### **Steps:**
1. Create a `Projects` table and insert sample data.
2. Use a `JOIN` to combine employee and project information through the department field.

### **Key Concepts:**
- `INNER JOIN`: Retrieves records with matching values in both tables.
- `LEFT JOIN`: Retrieves all records from the left table and matching records from the right.

### **SQL Example: Create and Populate a Projects Table**
```sql
CREATE TABLE Projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);

INSERT INTO Projects (name, department) VALUES
('Project A', 'HR'),
('Project B', 'IT'),
('Project C', 'Finance');
```

### **SQL Example: Complex JOIN**
List employees working in departments responsible for a specific project:
```sql
SELECT Employees.name, Projects.name AS project_name
FROM Employees
JOIN Projects ON Employees.department = Projects.department
WHERE Projects.name = 'Project A';
```

---

## **8.3 Aggregation**

### **Overview**
Aggregation functions like `MIN()`, `MAX()`, `COUNT()`, and `AVG()` allow you to summarize data across groups.

### **Task:**
Calculate the minimum and maximum salaries and the number of employees in each department.

### **SQL Example:**
```sql
SELECT department_id, 
       MIN(salary) AS min_salary, 
       MAX(salary) AS max_salary, 
       COUNT(employee_id) AS num_employees
FROM Employees
GROUP BY department_id;
```

### **Key Notes:**
- Use `GROUP BY` to organize results by department.
- Ensure fields in the `SELECT` clause are either aggregated or part of the `GROUP BY`.

---

## **8.4 Aggregation with HAVING**

### **Overview**
The `HAVING` clause filters aggregated results after the `GROUP BY` operation.

### **Task:**
List all departments where the average salary exceeds 70,000 and display the department manager.

### **SQL Example:**
```sql
SELECT d.department_name, 
       d.manager_id, 
       AVG(e.salary) AS avg_salary
FROM Departments AS d
JOIN Employees AS e ON d.department_id = e.department_id
GROUP BY d.department_id
HAVING AVG(e.salary) > 70000;
```

### **Key Notes:**
- Use `HAVING` instead of `WHERE` to filter aggregated results.
- Combine `JOIN`s and `GROUP BY` for advanced aggregations.

---

## **8.5 Performance Optimization: Indexing**

### **Overview**
SQL queries can sometimes be slow if they involve large tables. Indexes can be created on columns that are frequently used in `WHERE`, `JOIN`, or `ORDER BY` clauses to speed up query performance.

### **SQL Example:**
```sql
CREATE INDEX idx_department ON Employees(department_id);
```

This creates an index on the `department_id` column to speed up queries that filter by department.

---

## **8.6 Transactions and Rollbacks**

### **Overview**
Transactions ensure that multiple database operations are completed successfully before committing them. If an error occurs, you can roll back the changes to keep the database in a consistent state.

### **Example:**
```python
# Start a transaction
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO Employees (name, department_id) VALUES ('John Doe', 2)")
    cursor.execute("INSERT INTO Employees (name, department_id) VALUES ('Jane Smith', 3)")
    conn.commit()  # Commit transaction
except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)

conn.close()
```

---

## **8.7 Parameterized Queries to Prevent SQL Injection**

### **Overview**
SQL injection can be prevented by using parameterized queries, ensuring that user input is treated safely.

### **Example:**
```python
cursor.execute("SELECT * FROM Employees WHERE department_id = ?;", (department_id,))
```

This ensures that `department_id` is treated as a parameter and not part of the SQL statement itself.  If any part of the SQL statement comes from the end user or other untrusted source, always put that part in a parameter so that it can be sanitized to strip out rogue SQL.  Don't do it like this:

```python
cursor.execute(f"SELECT * FROM Employees WHERE department_id = {department_id};")
# or, equally bad:
cursor.execute("SELECT * FROM Employees WHERE department_id = " + department_id + ";")
```

---

## **8.8 Window Functions**

### **Overview**
SQL window functions allow for advanced analysis over a specified range of rows. For example, calculating the rank of employees within a department based on salary.

### **SQL Example:**
```sql
SELECT name, salary, department_id,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
FROM Employees;
```

---

## **8.9 Date and Time Functions**

### **Overview**
SQL provides functions for manipulating and querying date and time data, which are useful when working with time-based analysis.

### **SQL Example:**
```sql
SELECT name, date_of_birth, 
       JULIANDAY('now') - JULIANDAY(date_of_birth) AS age_in_days
FROM Employees;
```

---

## **8.10 Implementing All Techniques in Python**

### **Implementation Tips**

1. **Test Queries Separately:**
   - Write and test each query independently in your script or database interface before integrating into Python.

2. **Iterative Debugging:**
   - Verify intermediate outputs (e.g., after `JOIN` or subquery execution).

3. **Error Handling in Python:**
   - Use `try-except` blocks to handle database connection errors.

### **Example Python Script:**
```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Aggregation with HAVING
query = """
SELECT d.department_name, 
       d.manager_id, 
       AVG(e.salary) AS avg_salary
FROM Departments AS d
JOIN Employees AS e ON d.department_id = e.department_id
GROUP BY d.department_id
HAVING AVG(e.salary) > 70000;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print(results)

conn.close()
```

---

## **Summary**

In this lesson, you’ve learned:
1. How to use subqueries to dynamically fetch values for other queries.
2. How to use complex `JOIN`s to integrate data from multiple tables.
3. How to use aggregation functions to summarize data across groups.
4. How to apply `HAVING` for conditional filtering on aggregated data.
5. How to optimize performance with indexes.
6. How to use transactions and rollbacks to ensure data consistency.
7. How to prevent SQL injection with parameterized queries.
8. How to use window functions for advanced analytics.
9. How to handle date and time data for time-based analysis.

For further exploration, refer to the [SQLite Documentation](https://www.sqlite.org/docs.html) and Python's `sqlite3` library documentation.
