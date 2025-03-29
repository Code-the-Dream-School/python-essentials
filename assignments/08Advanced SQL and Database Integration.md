
# **Advanced SQL and Database Integration**

---

## **Lesson Overview**

**Learning Objective**:  
Students will deepen their understanding of SQL by learning advanced techniques such as subqueries, complex `JOIN`s, aggregation with functions, and using the `HAVING` clause for conditional filtering.

---

## **Assignment Instructions**

You create the code for this assignment in your python_homework/assignment8 folder.  You may want to have two VSCode terminal sessions.  In one, you have changed directories to `assignment8`.  This is the session where you will run your code.  In the other terminal session, you will run `sqlcommand.py` from the `python_homework` folder.  You need to have the working directory set differently, so that each program will be able to find `db/lesson.db`.  Be sure to create an `assignment8` git branch before you start.  As usual, mark the code that completes each task with a comment line.

### **Preparation and Practice**

You have already experimented with the `sqlcommand.py` program.  Run it again, and practice what you've learned.  You can do SELECT, INSERT, UPDATE and DELETE.  The SELECT statements can have JOIN, GROUP BY, ORDER BY, subqueries, HAVING, etc.  Practice these until you feel familiar with them.

For each of the following tasks, you first use the sqlcommand command line to get the right SQL statement.  Then you add it to your program.

**Help Available!**  

This lesson combines a lot of concepts that have been presented only briefly. You may find these tasks a little challenging.  If you get stuck, 1:1 mentors are available to answer your questions.  Appointments are available in the [1:1 Mentor Table](https://airtable.com/appoSRJMlXH9KvE6w/shrQinGb1phZYwdiL)

### **Task 1: Understanding Subqueries**

1. **Problem Statement**:  
   For each of the first 5 orders (as ordered by order_id), find the each of the product names for the order.  Return a list that includes the order_id, the line_item_id, and the product name.  There are several steps here.  You need a subquery to retrieve the order_id for the first 5 orders.  In this subquery, you use `ORDER BY order_id` and `LIMIT 5`.  In the main query, you need to select the order_id, line_item_id, and product_name from the orders table, the line_items table, and the products table.  Then you need a WHERE clause: `WHERE o.order_id IN (...)`.  The subquery is what returns the set of order_ids you want to check.

2. **Deliverable**: 
   - Within the python_homework folder, create an `assignment8` branch.
   - Get the SQL statement working in sqlcommand.
   - Within the python_homework directory, create `advanced_sql.py`. This opens the database, issues the SQL statement, prints out the result, and closes the database.
   - test your program.

---

### **Task 2: Complex JOINs with Aggregation**

1. **Problem Statement**:  
   Find the total price of each of the first 5 orders.  Again, there are several steps.  You need to join the orders table with the line_items table and the products table.  You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of the product price times the line_item quantity.  Then, you ORDER BY order_id and LIMIT 5.  You don't need a subquery. Print out the order_id and the total price for each of the rows returned.

2. **Deliverable**:  
   - Again, get the SQL statement working in sqlcommand.
   - Add code to `advanced_sql.py` to print out the result.

---

### **Task 3: An Insert Transaction Based on Data**

1. **Problem Statement**:  
   You want to create a new order for the customer named Perez and Sons.  The employee creating the order is Miranda Harris.  The customer wants 10 of each of the 5 least expensive products.  You first need to do a SELECT statement to retrieve the customer_id, another to retrieve the product_ids of the 5 least expensive products, and another to retrieve the employee_id.  Then, you create the order record and the 5 line_item records comprising the order.  You have to use the customer_id, employee_id, and product_id values you obtained from the SELECT statements. You have to use the order_id for the order record you created in the line_items records. The inserts must occur within the scope of one transaction. Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.

   You want to make sure that the foreign keys in the INSERT statements are valid.  So, add this line to your script, right after the database connection:
   ```
   conn.execute("PRAGMA foreign_keys = 1")
   ```

   In general, when creating a record, you don't want to specify the primary key.  So leave that column name off your insert statements.  SQLite will assign a unique primary key for you.  But, you need the order_id for the order record you insert to be able to insert line_item records for that order.  You can have this value returned by adding the following clause to the INSERT statement for the order:
   ```
   RETURNING order_id
   ```

2. **Deliverable**:   
   - Get this working in sqlcommand.  (Note that sqlcommand does not provide a way to begin and end transactions, so for sqlcommand, the creation of the order and line_item records are separate transactions.)
   - Use sqlcommand to delete the line_items records for the order you created.  (This is one delete statement.)  Delete also the order record you created.
   - Add statements for the complete transaction and the subsequent SELECT statement into `advanced_py.sql`, and to print out the result of the SELECT.
   - Test your program.

---

### **Task 4: Aggregation with HAVING**

1. **Problem Statement**:  
   Find all employees associated with more than 5 orders.  You want the first_name, the last_name, and the count of orders.  You need to do a `JOIN` on the employees and orders tables, and then use GROUP BY, COUNT, and HAVING.

2. **Deliverable**:  
   - Get it working in sqlcommand.
   - Add code `advanced_sql.py` to print out the employee_id, first_name, last_name, and an order count for each of the employees with more than 5 orders.
   - Test your program.

### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment8` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment8` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**. 

---

### **Resources**
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python `sqlite3` Library Documentation](https://docs.python.org/3/library/sqlite3.html)
```
