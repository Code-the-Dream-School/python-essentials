
# **Lesson 07 — Introduction to Databases and SQL**

## **Lesson Overview**
**Learning objective**: Students will gain foundational knowledge of SQL databases using Python and SQLite. They will define relational schemas, insert and query data using SQL, handle many-to-many relationships, and interact with databases directly from Pandas for analysis and reporting.

**Topics**:
1. Introduction to SQL: What SQL is, why relational databases matter, and how constraints, associations, and transactions work.
2. SQLite Setup: Installing dependencies (Windows only) and connecting to a local SQLite database.
3. Defining Tables: Creating tables with `CREATE TABLE` statements and specifying primary keys, foreign keys, and constraints.
4. Populating Tables: Using `INSERT INTO`and parameterized queries to add data to tables.
5. Querying Data: Writing `SELECT` queries, using `WHERE`, `ORDER BY`, and comparison operators.
6. Foreign Keys and Relationships: Creating and managing associations using `JOIN` tables.
7. Joins and Complex Queries: Writing multi-table joins with `JOIN`, `LEFT JOIN`, and `AS` aliases.
8. Modifying Data: Updating and deleting records using `UPDATE` and `DELETE` statements.
9. SQL Practice: Practicing queries using the `sqlcommand.py` interface and exploring a sample dataset.
10. Using SQL with Pandas: Loading SQL query results directly into Pandas DataFrames using `pd.read_sql_query()`.
11. (Optional) Additional Practice: Guided practice via the SQLBolt tutorial.

## **Setup**

An additional package is needed for this lesson, but ONLY ON WINDOWS.  Do not install this package if you are on a Mac or Linux, because on those platforms, the capability is part of the Python base.  If you are on Windows, then within the VSCode terminal of your `python_homework` folder, type:

```bash
pip install pyreadline3
```

### **Topics:**

1. What SQL Is, and Why it is Used
2. Creating a New SQLite Database
3. Defining the Database Structure
4. Populating Tables with Data
5. Writing SQL Queries
6. Creating Entries with Foreign Keys
7. More complicated queries, incuding JOINs
8. The UPDATE Statement
9. The Delete Statement
10. SQL Query Practice
11. SQL from Pandas
12. (Optional) More SQL Practice

---

## **7.1 What SQL Is, and Why it is Used**

SQL is the language used to access relational databases.  In a relational database, the data is stored in tables, each of which looks like a spreadsheat.  The database has a schema, and for each table in the database, the schema describes the columns in each table, giving each a name and a datatype.  There aren't many datatypes in a relational database.  We'll use SQLite, and SQLite only supports TEXT, NUMERIC, INTEGER, REAL, or BLOB datatypes.  Other datatypes are supported in SQLite by mapping them to one of these four.  (Other SQL implementations support more.)  One can compare this to no-SQL databases like MongoDB, when you can store any JSON document you like.  The schema can seem like a straitjacket, but it is really more a set of rails, organizing data into a structured form.

Read the following introduction: <https://www.theodinproject.com/lessons/databases-databases-and-sql>.  Or, if you know this stuff, jump to the bottom of that page and do the Knowledge Check.  Be sure that you understand the concepts of Primary Key and Foreign Key.

There are two important words left out of that introduction: Association and Transaction.

### **Associations**

An association exists between tables if one table has a foreign key that points to the other.  Consider the following cases:

1. An application has a `users` table and a `user_profiles` table.  Each record in the `user_profiles` table has a foreign key, which is the primary key of a record in the `users` table.  This is a one-to-one association.
2. An application has blogs.  Each blog has a series of posts.  The application might have a `blogs` table and a `posts` table.  Each record in the `posts` table would have a foreign key for a `blogs` table record, indicating the blog to which it belongs.  This is a one-to-many association, as one blog has many posts.
3. A magazine publisher has magazines and subscribers.  Each subscriber may subscribe to several magazines, and each magazine may have many subscribers.  Now we have a problem.  
We can't put a list of subscribers into a magazine record. Relational database records can't contain lists.  For a given magazine, we could create one record for each subscriber, but we'd be duplicating all the information that describes the magazine many times over.  Similarly, there is no way for the `subscribers` table to contain records for each magazine for each subscriber.  So, you need a table in the middle, sometimes called a **join table**.  In this case, the join table might be `subscriptions`.  Each subscription record has two foreign keys, one for the magazine and one for the subscriber.  This is a many-to many association.

### **Transactions**

A transaction is a write operation on an SQL database that guarantees consistency.  Consider a banking operation.  A user wants to transfer money from one account to another.  The sequence of SQL operations is as follows (this is pseudocode of course):

- Begin the transaction.
- Read the amount in account A to make sure there's enough.
- Update that record to decrease the balance by the desired amount.
- Update that record to increase the balance by the desired amount.
- Commit the transaction

The transaction maintains consistency.  When the read occurs, that entry is locked. (This depends on the isolation level and other stuff we won't get into now.)  That lock is important, as otherwise there could be another withdrawal from the account that happens after the read but before the update, and the account would go overdrawn.  Neither do you want the update that decreases the balance to complete while the update that increases the balance in the other account fails.  That would anger the user, and justifiably so.  With transactions, either both write operations succeed or neither succeeds.

Relational databases' strength, by comparision with no-SQL databases, is the efficient handing of structured and interrelated data and transactional operations on that data.

### **Constraints**

When a table is defined in the schema, one or several **constraints** on the values may also be specified.

- Datatype constraints: One constraint comes from the datatype of the column: you can't put a TEXT value in an INTEGER column, etc.  
- NOT NULL constraint:  When present, it means that whenever a record is created or updated, that column in the record must have a value.  
- UNIQUE constraint: You wouldn't want several users to have the same ID for example.  
- FOREIGN KEY constraint.  In the blog example above, each post must belong to a blog, meaning that the post record has the blog's primary key as a foreign key.  Otherwise you'd have a post that belonged to no blog, a worthless situation.

If you try to create a record that doesn't comply with constraints, or update one in violation of constraints, you get an exception.

SQLite, by default, does not turn on the foreign key constraint, but in the examples below, and in most real world situations, you will.

---

## **7.2 Creating a New SQLite Database**

### **Overview**

SQLite is a file-based database, meaning the database itself is stored in a file on disk. Python's `sqlite3` module allows easy interaction with SQLite databases.  It is built into Python, so there is nothing more to install.

### **Creating a Database:**

The `sqlite3.connect()` statement in Python creates a database if it does not exist.  Then it connects to that database.

1. Open VSCode for your `python_homework` folder.  As you will create files as part of the lesson, create your `assignment7` branch now.
2. Open your code editor within your `python_homework/assignment7` folder.  Create a new Python script file called `school_a.py`.  In your VSCode terminal, `cd` to the assignment7 folder.
3. Add the following code to that program to create or connect to a new SQLite database.

### **Example Code:**

```python
import sqlite3

# Connect to a new SQLite database
with  sqlite3.connect("../db/school.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
    print("Database created and connected successfully.")

# The "with" statement closes the connection at the end of that block.  You could close it explicitly with conn.close(), but in this case
# the "with" statement takes care of that.

```
Run the program to create a database.

**Outcome:**

Running the script creates a `school.db` file in the db folder.

## **7.3 Defining the Database Structure**

### **Overview**

Databases store structured data in tables. SQL queries allow you to define the schema of the tables by specifying columns, data types, and relationships.

### **Steps:**

1. Use SQL `CREATE TABLE` statements to define the structure of your database.  This code is added to `school_a.py`.  **Note** It is best to use `CREATE TABLE IF NOT EXISTS`, as in the example code that follows this section.  Otherwise your code will fail the second time you run it, as the table already exists.
2. Execute these queries within your Python script using the `execute()` method of a database cursor.

**Tables:**

- **Students:** Contains `student_id`, `name`, `age`, and `major`.
- **Courses:** Contains `course_id`, `course_name`, and `instructor_name`.
- **Enrollments:** Contains `enrollment_id`, `student_id`, and `course_id`.

### **Example Code:**

```python
import sqlite3

# Connect to the database
with sqlite3.connect("../db/school.db") as conn:
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        age INTEGER,
        major TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL UNIQUE,
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

2. What kind of association exists between Students and Courses?

Answers:

1. A student may have several or many enrollments, but for each enrollment there is only one student.  This is a one-to-many association between Students and Enrollments.  The student_id is the foreign key.

2. A student may enroll in many courses, and a given course may have many students enrolled.  This is a many-to-many association.  The Enrollments table acts as the join table to tie the two together, and both of its foreign keys are needed to manage the association.

## **7.4 Populating Tables with Data**

### **Overview**

Populating tables with data helps simulate real-world scenarios, allowing you to practice querying data. Use the `INSERT INTO` SQL query to insert sample records into your tables.

### **Steps:**

1. Create a file in the assignment7 folder called `school_b.py`. Within it, connect to the database, create a curson, and use SQL `INSERT INTO` queries to add data to the tables.
2. Add a commit() statement

### **Example Code:**

```python
import sqlite3 

# Connect to the database
with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bob', 22, 'History')") 
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")
```
Note that you do not have to specify the primary keys (student_id and course_id), although you can.  If you don't specify the primary keys, these are chosen for you, and the primary key column will never be null and will always have unique values.  If you do specify the primary keys, they have to be unique -- there can be no record in that table with the same primary key, or you get an exception.  You notice that there is no 'begin' statement for the commit.  By default, SQLite begins a transaction for you automatically.

At this point, you should install the SQLite Viewer plugin for your VSCode.  Once you've done that, open the db/school.db file in VSCode, and the tables you have created are displayed, along with any data you have added.

The INSERT statement can insert several rows in one statement.  You specify multiple sets of values for each of the columns, as follows (you don't need to add this to your program):
```python
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science'), ('Bob', 22, 'History')")
```

Now, you'd like to insert into the Enrollments table as well -- but, each enrollment record has foreign keys, which are primary keys from the Students and Courses tables.  You didn't choose the primary keys above, so you don't know what they are.  You'll solve that problem below.

### Check for Understanding

1. What happens if you try to run your program twice?

Answer:

1. You get an exception!  Student and course names must be unique.  You need to handle the exceptions!  So change your code as follows:

But, you still get an exception, for the next Insert.  You need to add the try/except for each of the insert statements.  This seems to violate the DRY principle (Do not Repeat Yourself).  You solve this by creating functions, as follows

```python
import sqlite3 

# Connect to the database

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Alice', 20, 'Computer Science')  
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")
```

The code above uses a **parameterized statement**.  You have `?` markers in the original SQL.  You pass a tuple as a second parameter for the `cursor.execute()`, and the values from the tuple are plugged into the statement in place of the `?` markers.

## **7.5 Writing SQL Queries**

### **Overview**

SQL queries allow you to interact with and analyze data. You will learn how to use SQL commands to retrieve and manipulate data.

**Queries:**

The SQL statements in this lesson, unless included in Python code, are just examples -- you do not need to add these to your code.

- Retrieve all student information:

```sql
SELECT * FROM Students;
```

- Find courses taught by a specific instructor:

```sql
SELECT * FROM Courses WHERE instructor_name = 'Dr. Smith';
```

- Find only the student_ids and names from the Student table:

```sql
SELECT student_id, name FROM Students;
```

- List students ordered by age:

```sql
SELECT * FROM Students ORDER BY age;
```

- Find the students of a given age majoring in English:

```sql
SELECT * FROM Students WHERE age = 22 AND major = 'History';
```

Within Python, SQL SELECT statements are executed like the INSERT statements, but you also need to retrieve the results.  Add the following to your school_b.py program:

```python
    cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")
    result = cursor.fetchall()
    for row in result:
        print(row)
```
When the SELECT statement is executed, it makes a collection of rows available.  The fetchall() creates an iterable connection of the matching rows, and each row is a tuple of the values from the requested columns.  In this case, you are using '*' which means all columns.  In this case, the first row returns the record for "Alice", and the first element in the tuple is the student_id.

## **7.6 Adding Entries with Foreign Keys**

Now you are ready to add enrollments, because you can resolve the primary keys that are used as foreign keys in the Enrollments table.  The steps are:

1. Find the student_id for the student.

2. Find the course_id for the course.

3. Insert the enrollment record.

You are going to do this for various students and courses, so again you create a function.  Add this code to school_b.py:

```python
def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

    ... # And at the bottom of your "with" block

    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")
    conn.commit() # more writes, so we have to commit to make them final!
```

Try this out, and then view the database in VSCode to see if the entries are created.  You may have to close your view of `school.db` and open it again to see your changes.

You could add exception handling, but it is not clear which exceptions you might get at this point, so it's not easy to add appropriate exception handling.

### Check for Understanding

1. What would happen if you tried the following:
    ```python
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) (95, 43)")
    ```

2. Try running school_b.py again, and check what happens with Enrollments.  You get duplicate records!  Duplicate, that is, except for the enrollment_id.  How could you prevent this?

Answer:

1. The foreign key constraint is ON!  You would get an exception.  There is no record in the Students table with a student_id of 95.  There is no record in the Courses table with a course_id of 43, so the foreign key constraint prevents this invalid record from being created.

2. You can't add another UNIQUE constraint to fix this problem, because you need to reuse the course_id and student_id values in multiple records.  But, you can check to see if the record already exists before you do the insert, as follows:

    ```python
    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Student {student} is already enrolled in course {course}.")
        return
    ```
    Try this out!

## **7.7 More Complicated Queries**

In the WHERE clause, you can use various comparison operators such as `< > <= >= <>`.  The `<>` means not equals.  You can also do math, such as `quantity * price`.  And, you can use the LIKE operator to find strings with the `%` sign used as a wildcard.  For example, to find all the math courses, you could do this:

```sql
SELECT * FROM Courses WHERE course_name LIKE "math%";
```
### Joins

A join is used within a SELECT statement to combine two or more tables.  The records returned from the SELECT include columns from both tables.  Joins use an ON clause to pair up the entries from each table.  The following SELECT gets the pairs of student name and course name, according to Enrollments, which is the join table.
```sql
SELECT Students.name, Courses.course_name FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id JOIN Courses ON Enrollments.course_id = Courses.course_id
```
The statement creates a combined row.  For each Student record, the Enrollments for that student are retrieved, and a combined record is created for any matches that are found.  The `ON` clause gives the matching logic.  Then, for each of these combined records, the corresponding Course record is retrieved, and added to the row.  The SELECT returns the name from the Students table and course_name from the Course table.  We can use 'AS' to save typing:

```sql
SELECT s.name, c.course_name FROM Students AS s JOIN Enrollments AS e ON s.student_id = e.student_id JOIN Courses AS c ON e.course_id = c.course_id;
```
And, one can even leave out the `AS`:
```sql
SELECT s.name, c.course_name FROM Students s JOIN Enrollments e ON s.student_id = e.student_id JOIN Courses c ON e.course_id = c.course_id;
```

Suppose you want to include customers that have done no orders.  You do a LEFT JOIN (because the customer table is on the left in the join statement.)
```sql
SELECT c.customer_name, o.order_id FROM customers c LEFT JOIN orders o on c.customer_id = o.customer_id;
```
If there are customers without orders, this statement will include them in the list, but the order_id column will be empty.  Similarly, one can do a RIGHT JOIN to show the orders without customers ... but there won't be any.  Why? Because the foreign key constraint is on, so you can't have an order record that doesn't belong to a customer.  You can also do a FULL JOIN to get both customers without orders and orders without a corresponding customer.

Suppose we want to list all the students with the corresponding courses for which they are enrolled.  There is, in this case, a many-to-many association between students and courses -- but there is no foreign key in either table that points to the other table.  We need to use the Enrollments table as a join table, combining information from all three tables.  This is a compound join.  You may join three or more tables in this way.

```sql
SELECT Students.name, Courses.course_name 
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id;
```

### **Check for Understanding**

1. We see that the JOIN statement for Students and Enrollments has an ON clause with Students.student_id = Enrollments.student_id.  Why doesn't it use Enrollments.enrollment_id?

Answer:

2. The enrollment_id doesn't correspond to anything in the Students table.  You have to use the foreign key, student_id, from the Enrollments table.  An ON cause typically combines a primary key (Students.student_id) with a foreign key (Enrollments.student_id).  By the way, the primary key doesn't have to have the same name as the foreign key.  If the primary key in the Students table were named `id`, you'd do `ON Students.id = Enrollments.student_id`.

### **Example Code:**

Of course, any of the SQL above can be executed from Python.


## **7.8 The UPDATE Statement**

The UPDATE SQL statement changes one or more existing rows.  You specify the rows you want to change with a WHERE clause, like you would use in a SELECT statement.

```sql
UPDATE Students SET name="Charles", age=20 WHERE name="Charlie";
```
Note that the UPDATE statement updates all rows that match the WHERE clause.  You can also apply math functions to the update, as follows:

```sql
UPDATE products SET price=price * 1.1;
```
This statement raises all the prices by 10%.  As there is no WHERE statement, every record is changed.

## **7.9 The DELETE Statement**

The DELETE Statement deletes one or more existing rows.  For example, the following statement deletes all product records if the price is less than 1.00:

```sql
DELETE FROM products WHERE price<1.0;
```
If you leave off the WHERE clause, it deletes every record in the table!

### **A Reference**

This is a very brief and incomplete summary of the SQL language.  The SQLBolt tutorial mentioned below gives more complete instruction, and a very good reference is available here: <https://www.w3schools.com/sql/default.asp>.  Some advanced topics, such as aggregation and subqueries, are discussed in the next lesson.

## **7.10 SQL Query Practice**

Your python_homework folder contains a program called `load_db.py`.  Take a look at its contents.  It creates a series of tables, for employees, customers, orders, products, and order_details.  Each order is associated with a customer and an employee.  For each order, there are line_items associated with the order, one line item for each product comprising the order.  You'll see the schema created at the top of the file.  Then, the file uses pandas to load data for each table from csv files into the database.  The resulting database is stored as `./db/lesson.db`.

Change the directory to the python_homework folder and run the `load_db.py` program to create and populate the database.  You can run it again as needed to restore the database to its initial state.  Next, run the `sqlcommand.py` program.  This prompts you with a command line you can use to enter SQL statements.  (Each statement must end with a semicolon.)  Experiment with various SELECT, INSERT, UPDATE, and DELETE statements.  Have a look at the code in `sqlcommand.py` to see how it works.

## **7.11 SQL from Pandas**

How does a data analyst use SQL?

You have learned how to load a Pandas DataFrame from a CSV file.  A limitation of CSV files is that they are static.  Each reflects data as it was some time in the past, when the file was written.  Suppose you want to use Pandas to analyse the baseball standings.  These change from day to day -- but instead of a CSV file, one can have a relational database with this information that is updated continuously.  You'd want to load that information into Pandas.  Fortunately, this is very easy. 

```python
import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)
```
This loads a dataframe from the results of a SELECT statement.  You then have access to all the statistical power of pandas.  In this case, we get a dataframe that lists all the customer names, all the orders, and the names of all the product that were ordered.  Note that there is a many-to-many association between orders and products, in that an order may have many products, but there may be many orders for a given product. The line_items table acts as a join table for orders and products.


## **7.12 Optional: More Practice**

An excellent tutorial on SQL is available at the following link: <https://sqlbolt.com/>.  This tutorial is optional, but it is **strongly recommended, including the More Topics section**.

### **Summary**
In this lesson, you learned:

1. How to create and connect to an SQLite database.
2. How to define tables using SQL queries.
3. How to populate tables with sample data.
4. How to write SQL queries to retrieve and analyze data.
5. How to commit changes and close the database connection.
6. How to modify and delete data.
7. How to access data from Pandas.
8. By mastering these techniques, you can efficiently interact with databases using Python. For further exploration, refer to the SQLite Documentation and Python’s sqlite3 library documentation.
