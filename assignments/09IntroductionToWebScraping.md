# **Introduction to Web Scraping**

### **Objective**

You learn to harvest data from a live web site, scraping values from the HTML page and storing them in a CSV file.

## **Assignment Instructions**

You create the code for this assignment in the assignment9 folder within your python_homework folder.  Be sure to create an `assignment9` git branch before you start.  As usual, mark the code that completes each task with a comment line.

---

## **Overview**
This lesson introduces web scraping concepts and practices, including:
1. Understanding HTML and the DOM structure in a live web page.
2. Extracting content using BeautifulSoup.
3. Storing data in CSV and JSON files.
4. Ethical considerations in web scraping.


---

## **Tasks**

### **Task 1: Review robots.txt to Ensure Policy Compliance**

In this assignment, you collect data from the Durham County Library site.  As always, when you do web scraping, you need to review the policy described in robots.txt, to ensure that you comply.

1. Open [https://durhamcountylibrary.org/robots.txt]

2. Verify that the following steps are not in breach of policy.

### **Task 2: Understanding HTML and the DOM for the Durham Library Site**

You are going to find where in the HTML page the data you want is located.

1. Open [https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart]

2. Open your browser developer tools to show the HTML elements.  For Chrome, this is `shift-ctrl-J`.

3. Find the HTML element for a single entry in the search results list.  This is a little tricky.  When you select an element in the Chrome developer tools, that part of the web page is highlighted.  But, that typically only gets you to the main `div`.  There is a little arrow next to that div in the developer tools element window, and you click on that to open it up to show the child elements.  Then, you select the element that corresponds to the search results area.  Continue in this way, opening up divs or other containers and selecting the one that highlights the area you want.  Eventually, you'll get to the first search result.  Hint: You are looking for an `li` element, because this is an element in an unordered list.  Note the values for the class attribute of this entry.  You'll want to save these in some temporary file, as your program will need them.

3. Within that element, find the element that stores the title.  Note the tag type and the class value.  Your program will need this value too, so save it too.

4. Within the search results `li` element, find the element that stores the author.  Hint: This is a link.  Note the class value and save it.  Some books do have multiple authors, so you'll have to handle that case.

5. Within the search results `li` element, find the element that stores the format of the book and the year it was published.  Note the class value and save it.  Now in this case, the class might not be enough to find the part of the `li` element you want.  So look at the `div` element that contains the format and year.  You want to note that class value too.

### **Task 3: Write a Program to Extract this Data**

1. Within the assignment9 diretory of your python_homework folder, create a program called `get_books.py`. The program should import `requests`, `BeautifulSoup`, and `pandas`.

2. Your program should then request the web page for the URL given in Task 2.

3. Your program should then parse the web page with BeautifulSoup.

4. Then, your program should find all the `li` entries in that page for the search list results.  You use the class values you stored in task 2 step 3.

5. Within your program, create an empty list called `results`.  You are going to add `dict` values to this list, one for each search result.

6. Main loop: You iterate through the list of `li` entries.  For each, you find the entry that contains title of the book, and get the text for that entry.  Then you find the entries that contain the authors of the book, and get the text for each.  If you find more than one author, you want to join the author names with a semicolon `;` between each.  Then you find the `div` that contains the format and the year, and then you find the `span` entry within it that contains this information.  You get that text too.  You now have three pieces of text.  Create a `dict` that stores these values, with the keys being `Title`, `Author`, and `Format-Year`.  Then append that `dict` to your `results` list.

7. Create a DataFrame from this list of dicts.  Print the DataFrame.

**Hint** You can put little print statements in at each step, to see if that part works.  For example, when you find all the `li` entries, you could print out the length of the list.  Then, you could just implement the part of the main loop that finds the Title, and just print out that title.  In this way, you can get the program done incrementally.

**For Further Thought**  You are getting the search results from the first page of the search results list.  How would you get all the search results from all the pages?  How can you make the program do this regardless of how many pages you might have?  **Optional:** Change your program to page through the search results so as to get all of the results.  However! You need to make sure your program pauses between pages.  Fast screen scraping, where many requests are sent in short order, is an abuse of the privilege.

### **Task 4: Write out the Data**
Modify your program to do the following:

1. Write the DataFrame to a file called `get_books.csv`, within the assignment9 folder.  Examine the file to see if it looks right.

2. Write the `results` list out to a file called `get_books.json`, also within the assignment9 folder.  You should write it out in JSON format.  Examine the file to see if it looks right.


### **Task 5: Ethical Web Scraping**

**Goal**:  
Understand the importance of ethical web scraping and `robots.txt` files.

1. Access the `robots.txt` file for Wikipedia: [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt).
2. Analyze the file and answer the following questions.  Put your answers in a file called `ethical_scraping.txt` in your python_homework/assignment9 directory
   - Which sections of the website are restricted for crawling?
   - Are there specific rules for certain user agents?
3. Reflect on why websites use `robots.txt` and write 2–3 sentences explaining its purpose and how it promotes ethical scraping.  Put these in `ethical_scraping.txt` in your python_homework directory.


---

### **Task 6: Scraping Structured Data**

**Goal**:  
Extract a web page section and store the information.

1. Within your python_homework/assignment9 directory, write a script called `see_also.py` to find the **"See also"** section of the Wikipedia page for screen scraping.  You'll have to use your browser developer tools to figure out how to find that section.

2. Once you have the tag for this section within your soup, Use the BeautifulSoup prettify() method to format the contents of that tag.  Print it out, and also write the resulting string to a file in the assignment9 folder called `see_also.html`.  Verify that this file appears correct.

3. Create a file, `challenges.txt`, also within your lesson9 directory.  In this file, describe any challenges you faced in completing this assignment and how you resolved them.

---



### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment9` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment9` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**. 

---

## **Resources**

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [MDN Web Docs: Understanding the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [Wikipedia Robots.txt](https://en.wikipedia.org/robots.txt)

---  
