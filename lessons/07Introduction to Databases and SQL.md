
# **Lesson 07 — Introduction to Databases and SQL**

## **Lesson Overview**

**Learning objective:** Students will gain foundational knowledge of databases and SQL by learning to create, populate, and query a SQLite database using Python. They will also understand how to manage database connections, commit changes, and use advanced SQL techniques.

### **Topics:**

1. What SQL Is, and Why it is Used
2. Creating a New SQLite Database
3. Defining the Database Structure
4. Populating Tables with Data
5. Writing SQL Queries
6. The UPDATE Statement
7. The Delete Statement
8. SQL Query Practice
9. SQL from Pandas
10. (Optional) More SQL Practice

---

## What SQL Is, and Why it is Used

SQL is the language used to access relational databases.  In a relational database, the data is stored in tables, each of which looks like a spreadsheat.  The database has a schema, and for each table in the database, the schema describes the columns in each table, giving each a name and a datatype.  There aren't many datatypes in a relational database.  We'll use SQLite, and SQLite, at bottom, has really only TEXT, NUMERIC, INTEGER, REAL, or BLOB.  One can compare this with no-SQL databases like MongoDB, when you can store any JSON document you like.  The schema can seem like a straightjacket, but it is really more a set of rails, organizing data into a structured form.

Read the following introduction: <https://www.theodinproject.com/lessons/databases-databases-and-sql>.  Or, if you know this stuff, jump to the bottom of that page and do the Knowledge Check.  Be sure that you understand the concepts of Primary Key and Foreign Key.

There are two important words left out of that introduction: Association and Transaction.

An association exists between tables if one table has a foreign key that points to the other.  Consider the following cases:

1. An application has a users table and a user_profiles table.  Each user_profiles record has a foreign key, which is the primary key of a record in the users table.  This is a one-to-one association.
2. An application has blogs.  Each blog has a series of posts.  The application might have a blogs table and a posts table.  Each entry in the posts table would have a foreign key for a blog, indicating the blog to which it belongs.  This is a one-to-many association, as one blog has many posts.
3. A magazine publisher has magazines and subscribers.  Each subscriber may subscribe to several magazines, and each magazine may have many subscribers.  Now we have a problem.  We can't put a list of subscribers into a magazine record. Relational database records can't contain lists.  For a given magazine, we could create one record for each subscriber, but we'd be duplicating all the information that describes the magazine many times over.  Similarly, there is no way for the subscribers table to contain records for each magazine for each subscriber.  So, you need a table in the middle, sometimes called a join table.  In this case, the join table might be subscriptions.  Each subscription record has two foreign keys, one for the magazine and one for the subscriber.  This is a many-to many association.

A transaction is a write operation on an SQL database that guarantees consistency.  Consider a banking operation.  A user wants to transfer money from one account to another.  The sequence of SQL operations is as follows (this is pseudocode of course):

- Begin the transaction.
- Read the amount in account A to make sure there's enough.
- Update that record to decrease the balance by the desired amount.
- Update that record to increase the balance by the desired amount.
- Commit the transaction

The transaction maintains consistency.  When the read occurs, that entry is locked. (This depends on the isolation level and other stuff we won't get into now.)  That lock is important, as otherwise there could be another withdrawal from the account that happens after the read but before the update, and the user would go overdrawn.  Also, you do not want the update that decreases the balance to complete while the update that increases the balance in the other account fails.  That would anger the user, and justifiably so.  Either each succeeds or neither.

Relational databases's strength, by comparision with no-SQL databases, is the efficient handing of structured and interrelated data and transactional operations on that data.

When a table is defined in the schema, **constraints** on the values may also be specified.  One constraint comes from the datatype of the column: you can't put a string in an integer column, etc.  In addition, there may be a NOT NULL constraint, which means that whenever a record is created or updated, that column in the record must have a value.  There may be a UNIQUE constraint: You wouldn't want several users to have the same ID for example.  And, there may be a FOREIGN KEY constraint.  In the blog example above, each post must belong to a blog, meaning that the post record has, as a foreign key, the blog's primary key.  Otherwise you'd have a post that belonged to no blog, a worthless situation.

If you try to create a record that doesn't comply with constraints, or update one in violation of constraints, you get an exception.

SQLite, by default, does not turn on the foreign key constraint, but in the examples below, and in most real world situations, you will.

---

## **7.2 Creating a New SQLite Database**

### **Overview**

SQLite is a file-based database, meaning the database itself is stored in a file on disk. Python's `sqlite3` module allows easy interaction with SQLite databases.  It is built into Python, so there is nothing more to install.

### **Steps to Create a Database:**

1. Open your code editor within the python_homework folder.  Create a new Python script file called `lesson07_a.py`.
2. Use the `sqlite3.connect()` method to create or connect to a new SQLite database. SQLite automatically creates the database file if it does not exist.

### **Example Code:**

```python
import sqlite3

# Connect to a new SQLite database
with  sqlite3.connect("./db/school.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
    print("Database created and connected successfully.")

# The with statement closes the connection at the end of that block.  You could close it explicitly with conn.close(), but in this case
# the with statement takes care of that.

```

**Outcome:**

Running the script creates a `school.db` file in the db folder.

## **7.3 Defining the Database Structure**

### **Overview**

Databases store structured data in tables. SQL queries allow you to define the schema of the tables by specifying columns, data types, and relationships.

### **Steps:**

1. Use SQL `CREATE TABLE` queries to define the structure of your database.  This code is added to `lesson07_a.py`.
2. Execute these queries within your Python script using the `execute()` method of a database cursor.

**Tables:**

- **Students:** Contains `student_id`, `name`, `age`, and `major`.
- **Courses:** Contains `course_id`, `course_name`, and `instructor_name`.
- **Enrollments:** Contains `enrollment_id`, `student_id`, and `course_id`.

### **Example Code:**

```python
import sqlite3

# Connect to the database
with sqlite3.connect("./db/school.db") as conn:
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        instructor_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students (student_id),
        FOREIGN KEY (course_id) REFERENCES Courses (course_id)
    )
    """)

    print("Tables created successfully.")
```

### Check for Understanding

1. What kind of association exists between Students and Enrollments?

2. What kine of association exists between Students and Courses?

Answers:

1. A student may have several or many enrollments, but for each enrollment there is only one student.  This is a one-to-many association between Students and Enrollments.  The student_id is the foreign key.

2. A student may enroll in many courses, and a given course may have many students enrolled.  This is a many-to-many association.  The Enrollments table acts as the join table to tie the two together, and both of its foreign keys are needed to manage the association.

## **7.4 Populating Tables with Data**

### **Overview**

Populating tables with data helps simulate real-world scenarios, allowing you to practice querying data. Use the `INSERT INTO` SQL query to insert sample records into your tables.

### **Steps:**

1. Create a file, `lesson07_b.py`. Use SQL `INSERT INTO` queries to add data to the tables.
2. Execute the queries within your Python script.  Add another `with` block, below the one that created the tables.

### **Example Code:**

```python
import sqlite3 

# Connect to the database
with sqlite3.connect("./db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bob', 22, 'History')") 
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 1)") 
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 2)") 
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (2, 1)") 
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (3, 3)") 

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")
```
The INSERT statement can insert several rows in one statement, as follows:
```python
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 1), (1,2), (2,1), (3,3);")
```
For the column names you specify, you can specify multiple sets of values.

### Check for Understanding

1. What would happen if you tried to execute the following line inside the `with` block above?

```python
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 123)")
```

2. What happens if you try to run your program twice?

Answers: 

1. The foreign key constraint is on!  123 is not a valid course_id, because it does not correspond to any course record.  You'd get an exception.  The exception happens when the INSERT statement runs, that is, before the commit statement is reached.

2. If you try running the program twice, you get an exception.  You can't create multiple records in a given table with the same primary key.  Primary keys have to be unique.

## **7.5 Writing SQL Queries**

### **Overview**

SQL queries allow you to interact with and analyze data. You will learn how to use SQL commands to retrieve and manipulate data.

**Queries:**

- Retrieve all student information:

```sql
SELECT * FROM Students;
```

- Find courses taught by a specific instructor:

```sql
SELECT * FROM Courses WHERE instructor_name = 'Dr. Smith';
```

In the WHERE clause, you can use various comparison operators such as `< > <= >= <>`.  The `<>` means not equals.  You can also do math, such as `quantity * price`.  And, you can use the LIKE operator to find strings with the `%` sign used as a wildcard.  Fir example, to find all the math courses, you could do this:
```sql
SELECT * FROM Courses WHERE course_name LIKE "math%";
```
### Joins

A join is used within a SELECT statement to combine several tables.  The records returned from the SELECT include columns from both tables.  Joins use an ON clause to pair up the entries from each table:
```sql
SELECT customers.customer_name, orders.order_id FROM customers JOIN orders ON customers.customer_id = orders.customer_id;
```
The above statement gives a list of customers along with their orders.  As there is a one-to-many association between customers and orders, there will be multiple rows for each customer, with one row for each order belonging to that customer.  There are two customer_id columns in the combined table, because the orders table contains the customer_id as a foreign key, so the join statement has to indicate which one we want, or you will get an error.  We can use `AS` for a shortcut:
```sql
SELECT c.customer_name, o.order_id FROM customers AS c JOIN orders AS o on c.customer_id = o.customer_id;
```
And, one can even leave out the `AS`:
```sql
SELECT c.customer_name, o.order_id FROM customers c JOIN orders o on c.customer_id = o.customer_id;
```

Suppose you want to include customers that have done no orders.  You do a LEFT JOIN (because the customer table is on the left in the join statement.)
```sql
SELECT c.customer_name, o.order_id FROM customers c LEFT JOIN orders o on c.customer_id = o.customer_id;
```
If there are customers without orders, this statement will include them in the list, but the order_id column will be empty.  Similarly, one can do a RIGHT JOIN to show the orders without customers ... but there won't be any.  Why? Because the foreign key constraint is on, so you can't have an order record that doesn't belong to a customer.  You can also do a FULL JOIN to get both customers without orders and orders without a corresponding customer.

Suppose we want to list all the students with the corresponding courses for which they are enrolled.  There is, in this case, a many-to-many association between customers and courses -- but there is no foreign key in either table that points to the other table.  We need to use the Enrollments table as a join table, combining information from all three tables.  This is a compound join.  You may join three or more tables in this way.

```sql
SELECT Students.name, Courses.course_name 
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id;
```

- List students ordered by age:

```sql
SELECT * FROM Students ORDER BY age;
```

### **Check for Understanding**

1. We see that the JOIN statement for customers and orders has an ON clause with customer.customer_id = orders.customer_id.  Why doesn't it use orders.order_id?

Answer:

2. The order_id doesn't correspond to anything in the customer table.  You have to use the foreign key, customer_id, from the orders table.  An ON cause typically combines a primary key (customer.customer_id) with a foreign key (orders.customer_id).

### **Example Code:**

Of course, any of the SQL above can be executed from Python.

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("./db/school.db")
cursor = conn.cursor()

# Execute and display query results
cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Courses WHERE instructor_name = 'Dr. Smith'")
print(cursor.fetchall())

conn.close()  # In this case the with statement is not being used, so the connection must be closed explicitly
```

## **7.6 The UPDATE Statement**

The UPDATE SQL statement changes one or more existing rows.  You specify the rows you want to change with a WHERE clause, like you would use in a SELECT statement.

```sql
UPDATE Students name="Charles", age=20 WHERE name="Charlie";
```
Note that the UPDATE statement updates all rows that match the WHERE clause.  You can also apply math functions to the update, as follows:

```sql
UPDATE products price=price * 1.1;
```
This statement raises all the prices by 10%.  As there is no WHERE statement, every record is changed.

## **7.7 The DELETE Statement**

The DELETE Statement deletes one or more existing rows.  For example, the following statement deletes all product records if the price is less than 1.00:

```sql
DELETE FROM products WHERE price<1.0;
```
If you leave off the WHERE clause, it deletes every record in the table!

### **A Reference**

This is a very brief and incomplete summary of the SQL language.  The SQLBolt tutorial mentioned below gives more complete instruction, and a very good reference is available here: <https://www.w3schools.com/sql/default.asp>.  Some advanced topics, such as aggregation and subqueries, are discussed in the next lesson.

## **7.8 SQL Query Practice**

Your python_homework folder contains a program called `load_db.py`.  Take a look at its contents.  It creates a series of tables, for employees, customers, orders, products, and order_details.  Each order is associated with a customer and an employee.  For each order, there are line_items associated with the order, one line item for each product comprising the order.  You'll see the schema created at the top of the file.  Then, the file uses pandas to load data for each table from csv files into the database.  The resulting database is stored as `./db/lesson.db`.

Run the `load_db.py` program to create and populate the database.  You can run it again as needed to restore the database to its initial state.  Next, run the `sqlcommand.py` program.  This prompts you with a command line you can use to enter SQL statements.  (Each statement must end with a semicolon.)  Experiment with various SELECT, INSERT, UPDATE, and DELETE statements.  Have a look at the code in `sqlcommand.py` to see how it works.

## **7.9 SQL from Pandas**

How does a data analyst use SQL?

You have learned how to load a Pandas DataFrame from a CSV file.  A limitation of CSV files is that they are static.  Each reflects the data as of some time in the past.  Suppose you want to use Pandas to analyse the baseball standings.  These change from day to day -- but one could have a relational database with this information that is updated continuously.  You'd want to load that information into Pandas.  Fortunately, this is very easy. 

```python
import pandas as pd
import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
```
This loads a dataframe from the results of a SELECT statement.  You then have access to all the statistical power of pandas.  In this case, we get a dataframe that lists all the customer names, all the orders, and the names of all the product that were ordered.  Note that there is a many-to-many association between orders and products, in that an order may have many products, but there may be many orders for a given product. The line_items table acts as a join table for orders and products.


## **7.10 Optional: More Practice**

An excellent tutorial on SQL is available at the following link: <https://sqlbolt.com/>.

### **Summary**
In this lesson, you learned:

1. How to create and connect to an SQLite database.
2. How to define tables using SQL queries.
3. How to populate tables with sample data.
4. How to write SQL queries to retrieve and analyze data.
5. How to commit changes and close the database connection.
6. By mastering these techniques, you can efficiently interact with databases using Python. For further exploration, refer to the SQLite Documentation and Python’s sqlite3 library documentation.
