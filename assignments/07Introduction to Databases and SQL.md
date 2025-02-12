Introduction to Databases and SQL**

For this assignment, you create code in your python_homework folder (not Kaggle this time.)


## **Task 1: Create a New SQLite Database**
1. Within your python_homework folder, create an `assignment7` branch.
2. Within that folder, create a file `sql_intro.py`.
2. Write code to connect to a new SQLite database, `./db/new.db` and to close the connection.
3. Execute the script and confirm the database file is created.  Note: All SQL statements should be executed within a try block, because they can raise exceptions.

---

## **Task 2: Define Database Structure**
1. Add SQL statements to `sql_intro.py` that create the following tables:
   - `Students`: Include fields for student ID, name, age, and major.
   - `Courses`: Include fields for course ID, course name, and instructor name.
   - `Enrollments`: Include fields for enrollment ID, student ID, and course ID.
   The student ID and course ID in the Enrollments table should be foreign keys.  Each of these values must correspond to actual records in the Students and Courses tables.
2. Add the SQLite Viewer to VSCode.
3. Run the script to execute the queries.
4. Open the `./db/new.db` file in VSCode to confirm that the tables are created.

---

## **Task 4: Populate Tables with Data**
1. Add the following line to sql_intro.py, right after the statement that connects to the database:
   ```
   conn.execute("PRAGMA foreign_keys = 1")
   ```
   This line tells SQLite to make sure the foreign keys are valid.
2. Add code to sql_intro.py to insert sample data into the `Students`, `Courses`, and `Enrollments` tables.  Don't forget to do a `conn.commit()` for your inserts!
2. Run the revised script.
3. Verify the data has been added by checking the database as displayed by VSCode.  Note: If you run your script again, an exception will be raised, because you are trying to reuse a primary key.  Primary keys in a table have to be unique.  You can delete `./db/new.db` before running your script to get around the problem.

---

## **Task 5: Write SQL Queries**
1. Write a query to retrieve all student information from the `Students` table.
2. Write a query to find courses taught by a specific instructor.
3. Write a query to retrieve student enrollments along with course names using a `JOIN`.
4. Write a query to list students ordered by age.
5. Add these queries to your script.  For each, print the result.  Note: You get the result by doing a
   ```
   result=cursor.fetchall()
   ```
   This returns an iterable collection of tuples, one for each row.  An interable collection works like a list.  You should loop through the collection and print each row.  Alternately, you can do a `cursor.fetchone()` to get the first (or next) row from the result.

## **Task 6: Read Data into a DataFrame**

1. While still within the python_homework directory, create a program, `sql_intro_2.py`.
2. The program should read all the orders for all the customers, to get all the products that each as ordered into a DataFrame.  The lesson shows how.
3. As some customers may have ordered the same product in several different orders, you want to combine the rows for these different orders.  You use the group_by() operation on the DataFrame to combine rows where the product_name and the customer_name are the same.
4. With the group_by(), use count() to show how many times each customer ordered a given product.
5. Print out the resulting DataFrame.  

---

### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment7` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment7` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**. 

---


