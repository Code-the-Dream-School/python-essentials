# **Lesson 10: Data Storage and Retrieval**

## **Assignment Instructions**

You create the code for this assignment in your python_homework/assignment10 folder.  Be sure to create an `assignment10` git branch before you start.  As usual, mark the code that completes each task with a comment line.

---

---

## **Task 1: Storing Data in JSON**
1. Within your assignment10 folder, Write a script called `store_page_to_json.py` to scrape data from another Wikipedia page of your choice.
2. The script should save the scraped data (title, headers, and links) into a JSON file called page.json.
3. Open the JSON file and verify its contents.

---

## **Task 2: Storing Data in CSV**
1. Within your assignment10 folder, write a script called `store_page_to_csv.py`.
2. The script shouldModify the script to include additional data (e.g., image sources).
2. Save the new data to a CSV file within the assignment10 folder called page.csv.
3. Test your script and verify the output.

---

## **Task 3: Storing Data in Databases**
1. Create a script called `page_to_db.py`. This should create a new SQLite database called `page.db`, with a table for storing scraped data from a different page.  Create the database within the db directory of your python_homework folder.
2. The script should write the data from the CSV file into the database.
3. Retrieve and print the data from the database.  Redirect the output to a file, `page_db.txt` so that it is submitted with your homework.  Note: Your database is not submitted with 

---

## **Task 4: Data Retrieval and Analysis with Pandas**
1. Load the stored data from your SQLite database into a Pandas DataFrame.
2. Perform the following analyses:
   - Count the number of headers and links.
   - Find the most frequent type of data.
3. Write a short summary of your findings.  Put that in a file called assignment10.txt.

---

## **Task 5: Optimizing Data Storage**
1. Research and write a short comparison between relational databases (e.g., SQLite) and non-relational databases (e.g., MongoDB).
2. Discuss which type of storage would be more suitable for:
   - A small-scale project like scraping Wikipedia.
   - A large-scale project involving millions of records.
   Add your thoughts to assignment10.txt.


---


### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment10` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment10` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**. 

---
