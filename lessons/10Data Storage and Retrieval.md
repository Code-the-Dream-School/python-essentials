
# **Lesson 10 — Data Storage and Retrieval**

## **Lesson Overview**
**Learning objective:** In this lesson, students will learn how to efficiently store and retrieve data using databases. The lesson will also cover how to manipulate and analyze the stored data using Python libraries such as Pandas and SQL. Additionally, students will gain insight into choosing the best storage solution based on different project scales and complexities.

### **Topics:**
1. Storing Scraped Data in Databases
2. Retrieving and Analyzing Data: SQL and Pandas
3. Optimizing Data Storage: Relational vs. Non-relational Databases
4. Exploring Data Retrieval Techniques: SQL Queries and DataFrame Operations
5. Using decorators in Python
---

## **10.1 Storing Scraped Data**

### **Overview**
After scraping data from the web, it’s essential to store it in a format that allows easy access and manipulation. The three most common formats are:
- **JSON:** A lightweight, human-readable format for structured data.
- **CSV:** A tabular format that is compatible with spreadsheets and easy to manipulate.
- **Databases:** Best suited for large, structured data that needs to be queried efficiently.

In the previous lesson you have stored data as JSON and CSV file, now we're going to take that data and input it into a sqlite database.


### **Storing Data in Databases**
It is common to use data frames when you are processing data from the internet, and then to save it as a database so that you are able to reference it in the future. This is because data frames are stored in memory, and data bases are saved on disk. Using this you are also able to process more data at once, without running into limits of your computers memory. 

1. Use SQLite to create a database table that can hold structured data.
2. Insert scraped data using SQL commands for easy retrieval and analysis.

#### **Example Code: Storing Data in a Database**
```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("scraped_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ScrapedData (
    id INTEGER PRIMARY KEY,
    header TEXT,
    link TEXT,
    image TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO ScrapedData (header, link, image) VALUES (?, ?, ?)",
               ("Introduction", "https://example.com/intro", "https://example.com/image1.png"))
conn.commit()

print("Data saved to the database.")
conn.close()
```

---

## **10.2 Retrieving and Analyzing Data**

### **Overview**
Once the data is stored, it’s important to retrieve it efficiently and analyze it to extract valuable insights. SQL and Pandas are two powerful tools that allow us to perform complex queries and data manipulations.

### **Retrieving Data from SQL**
1. Use SQL queries to fetch data from databases.
2. Store query results in a Pandas DataFrame for further analysis.

#### **Example Code: Retrieving Data into a Pandas DataFrame**
```python
import pandas as pd
import sqlite3

# Connect to the database and load data into a DataFrame
conn = sqlite3.connect("scraped_data.db")
query = "SELECT * FROM ScrapedData"
df = pd.read_sql_query(query, conn)

# Perform analyses
header_count = len(df['header'].unique())
link_count = len(df['link'].unique())

print(f"Number of unique headers: {header_count}")
print(f"Number of unique links: {link_count}")

conn.close()
```

---

## **10.3 Optimizing Data Storage**

### **Overview**
Choosing the right data storage type depends on the complexity, scale, and structure of the data. Understanding the advantages and limitations of relational and non-relational databases will help you select the best solution for your project.

### **Comparison: Relational vs. Non-relational Databases**

| Feature               | Relational (e.g., SQLite) | Non-relational (e.g., MongoDB) |
|-----------------------|--------------------------|--------------------------------|
| Data Structure        | Tables with rows/columns | Flexible document structure    |
| Query Language        | SQL                      | NoSQL or JSON-based queries    |
| Scalability           | Limited for large data   | High scalability               |
| Best Use Case         | Structured, small-scale  | Unstructured, large-scale      |

### **Key Points:**
- **Relational Databases** (SQLite, MySQL): Suitable for smaller projects with structured data that requires complex querying.
- **Non-relational Databases** (MongoDB, CouchDB): Best for large-scale projects with high-volume, semi-structured, or unstructured data, where flexibility is more important than strict relational structure.

---

## **10.4 Exploring Data Retrieval Techniques: SQL Queries and DataFrame Operations**

### **Overview**
Now that data is stored and accessible, it’s essential to retrieve it using efficient queries. You’ll also want to process and manipulate the data using powerful tools like Pandas.

### **Key Techniques:**
1. Use `SELECT` statements to retrieve specific columns and filter results.
2. Perform complex operations such as joins, aggregations, and sorting using both SQL and Pandas.

#### **Example Code: SQL Query with JOIN and Aggregation**
```python
# Example SQL query that joins tables and aggregates data
query = """
SELECT department_id, 
       MIN(salary) AS min_salary, 
       MAX(salary) AS max_salary, 
       COUNT(employee_id) AS num_employees
FROM Employees
GROUP BY department_id
HAVING COUNT(employee_id) > 5;
"""

# Execute and fetch results into a DataFrame
df = pd.read_sql_query(query, conn)
print(df)
```

#### **Pandas Aggregation Example:**
```python
# Example of Pandas aggregation
department_stats = df.groupby('department_id').agg(
    min_salary=('salary', 'min'),
    max_salary=('salary', 'max'),
    num_employees=('employee_id', 'count')
)
print(department_stats)
```

---
## **10.4 Exploring Data Retrieval Techniques: SQL Queries and DataFrame Operations**

### **Overview**
Python classifies functions as first class citizens, which means that you are able to apply one function to another function. Decorators allow this to be clearer and easier to read.
### **Key techniques**
Decorators are functions that can be called in a unique way, and accept a function as an input.

```Python3

def decorator(func):
    def wrapper():
        print ("Hello!")
        func()
        print ("World")
@decorator
def name():
    print("John")
```

Note in this example the output:
```
Hello!
John
World!
```

Why did we get this result? The answer is because @decorator called the function using the decorator function. It is effectively equivelent to calling
```python3
decorator(name())
```
but is much clearer and easier to understand.

In this example the function is fairly trivial, however in the next section we can dig into a more useful way to use this.
### **Example code**

We will be writting a decorator that allows us to benchmark different sections of code. We need to allow all functions to go into this decorator, and it will print out the time it took for a function to complete.
```python3
import time

def timer(func):
    ## Output the time the inner function takes
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print ("Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer
```



---
## **Summary**

In this lesson, you learned:
1. How to store scraped data using databases.
2. How to retrieve and analyze stored data using SQL and Pandas.
3. The differences between relational and non-relational databases and when to use each type.
4. Techniques for efficiently retrieving and analyzing data stored in databases.

For further reading, explore the [Python JSON Documentation](https://docs.python.org/3/library/json.html), [SQLite Documentation](https://www.sqlite.org/docs.html), and [Pandas Documentation](https://pandas.pydata.org/docs/).


