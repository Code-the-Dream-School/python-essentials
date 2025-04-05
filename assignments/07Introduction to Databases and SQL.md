Introduction to Databases and SQL**

For this assignment, you create code in your python_homework/assignment7 folder.


## **Task 1: Create a New SQLite Database**
1. Within your python_homework repository, create an `assignment7` git branch.
2. Make the `assignment7`  folder the working folder.  Within the `assignment7` folder, create a file `sql_intro.py`.
3. Write code to connect to a new SQLite database, `../db/magazines.db` and to close the connection.
4. Execute the script and confirm the database file is created.  Note: All SQL statements should be executed within a `try` block, followed by a corresponing `except` block, because any SQL statement can cause an exception to be raised.

---

## **Task 2: Define Database Structure**
We have publishers that publish magazines.  Each publisher has a unique name, and so does each magazine.  There is a one-to-many relationship between publishers and magazines.  We also have subscribers, and each subscriber has a name and an address.  We have a many-to-many association between subscribers and magazines, because a subscriber may subscribe to several magazines, and a magazine may have many subscribers.  So, we have a join table called subscriptions.  The subscriptions table also stores the expiration_date (a string) for the subscription.  All the names, the address, and the expiration_date must be non-null.  

1. Think for a minute.  There is a one-to-many relationship between publishers and magazines.  Which table has a foreign key? Where does the foreigh key point?  How about the subscriptions table: What foreigh keys does it have?

2. Add SQL statements to `sql_intro.py` that create the following tables:
   - `publishers`
   - `magazines`
   - `subscribers`
   - `subscriptions`
   Be sure to include the columns you need in each, with the right data types, with UNIQUE and NOT NULL constraints as needed, and with foreign keys as needed.  You can reuse column names if you choose, i.e. you might have a name column for publishers and a name column for magazines.  By the way, if you mess up this or the following steps, you can just delete `db/magazines.db`.

3. Open the `db/magazines.db` file in VSCode to confirm that the tables are created.

---

## **Task 3: Populate Tables with Data**
1. Add the following line to sql_intro.py, right after the statement that connects to the database:
   ```
   conn.execute("PRAGMA foreign_keys = 1")
   ```
   This line tells SQLite to make sure the foreign keys are valid.
2. Create functions, one for each of the tables, to add entries.  Include code to handle exceptions as needed, and to ensure that there is no duplication of information.  The subscribers name and address columns don't have unique values -- you might have several subscribers with the same name -- but when creating a subscriber you should check that you don't already have an entry where BOTH the name and the address are the same as for the one you are trying to create.
3. Add code to the main line of your program to populate each of the 4 tables with at least 3 entries.  Don't forget the `commit`!
4. Run the program several times.  View the database to ensure that you are creating the right information, without duplication.

---

## **Task 4: Write SQL Queries**
1. Write a query to retrieve all information from the subscribers table.
2. Write a query to retrieve all magazines sorted by name.
3. Write a query to find magazines for a particular publisher, one of the publishers you created.  This requires a `JOIN`. 
4. Add these queries to your script.  For each, print out all the rows returned by the query.

---

## **Task 6: Read Data into a DataFrame**

You will now use Pandas to create summary data from the `../db/lesson.db` database you populated as part of the lesson.  We want to find out how many times each product has been ordered, and what was the total price paid by product.

1. While still within the `python_homework/assignment7` directory, create a program, `sql_intro_2.py`.
2. Read data into a DataFrame, as described in the lesson.  The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price from a JOIN of the line_items table and the product table. Hint: Your `ON` statement would be `ON line_items.product_id = products.product_id`.
3. Print the first 5 lines of the resulting DataFrame.  Run the program to make sure this much works.
4. Add a column to the DataFrame called "total".  This is the quantity times the price.  (This is easy: `df['total'] = df['quantity'] * df['price']`.)  Print out the first 5 lines of the DataFrame to make sure this works.
5. Add groupby() code to group by the product_id.  Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'.  Print out the first 5 lines of the resulting DataFrame.  Run the program to see if it is correct so far.
6. Sort the DataFrame by the product_name column.
7. Add code to write this DataFrame to a file `order_summary.csv`, which should be written in the `assignment7` directory.  Verify that this file is correct.

As we'll learn in the next lesson, the ordering, grouping, count, and sum operations can be done in SQL, more efficiently than in Pandas.  The key concepts of pandas and SQL overlap very strongly.

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


