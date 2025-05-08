## Lesson 3 Assignment — Intro to Data Engineering
### Data Analysis and Manipulation with Pandas

### **Objective:**
In this assignment, you will explore the basic functionalities of the Pandas library in Python, including creating, manipulating, inspecting, and analyzing data using various DataFrame methods. The goal is to understand how to handle data efficiently and perform essential operations to inspect and analyze datasets.

### **Step 1: Complete the Coding Tasks**  

Homework for this assignment is created within your `python_homework` folder.  Create an `assignment3` branch and change to the `assignment3` folder.  Write your code in `assignment3.py`.  As with the previous lessons, you will run unit tests on the assignment `pytest -v -x assignment3-test.py`.

---

### **Tasks:**

### **Task 1: Introduction to Pandas - Creating and Manipulating DataFrames**
1. **Create a DataFrame from a dictionary:**
   - Use a dictionary containing the following data:
     - `Name`: ['Alice', 'Bob', 'Charlie']
     - `Age`: [25, 30, 35]
     - `City`: ['New York', 'Los Angeles', 'Chicago']
   - Convert the dictionary into a DataFrame using Pandas.
   - Print the DataFrame to verify its creation.
   - save the DataFrame in a variable called `task1_data_frame` and run the tests.

2. **Add a new column:**
   - Make a copy of the dataFrame you created named `task1_with_salary` (use the `copy()` method)
   - Add a column called `Salary` with values `[70000, 80000, 90000]`.
   - Print the new DataFrame and run the tests.

3. **Modify an existing column:**
   - Make a copy of `task1_with_salary` in a variable named `task1_older`
   - Increment the `Age` column by 1 for each entry.
   - Print the modified DataFrame to verify the changes and run the tests.

4. **Save the DataFrame as a CSV file:**
   - Save the `task1_older` DataFrame to a file named `employees.csv` using ```to_csv()```, do not include an index in the csv file.
   - Look at the contents of the CSV file to see how it's formatted.
   - Run the tests.
     

### **Task 2: Loading Data from CSV and JSON**
1. **Read data from a CSV file:**
   - Load the CSV file from Task 1 into a new DataFrame saved to a variable `task2_employees`.
   - Print it and run the tests to verify the contents.

2. **Read data from a JSON file:**
   - Create a JSON file (`additional_employees.json`).  The file adds two new employees.  Eve, who is 28, lives in Miami, and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
   - Load this JSON file into a new DataFrame and assign it to the variable `json_employees`.
   - Print the DataFrame to verify it loaded correctly and run the tests.

3. **Combine DataFrames:**
   - Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable `more_employees`.
   - Print the combined Dataframe and run the tests.

### **Task 3: Data Inspection - Using Head, Tail, and Info Methods**
1. **Use the `head()` method:**
   - Assign the first three rows of the `more_employees` DataFrame to the variable `first_three`
   - Print the variable and run the tests.

2. **Use the `tail()` method:**
   - Assign the last two rows of the `more_employees` DataFrame to the variable `last_two`
   - Print the variable and run the tests.

3. **Get the `shape` of a DataFrame**
   - Assign the shape of the `more_employees` DataFrame to the variable `employee_shape`
   - Print the variable and run the tests 

4. **Use the `info()` method:**
   - Print a concise summary of the DataFrame using the `info()` method to understand the data types and non-null counts.

### **Task 4: Data Cleaning**

1. Create a DataFrame from `dirty_data.csv` file and assign it to the variable `dirty_data`.
   - Print it and run the tests.
   - Create a copy of the dirty data in the varialble `clean_data` (use the `copy()` method).  You will use data cleaning methods to update `clean_data`.

2. Remove any duplicate rows from the DataFrame
   - Print it and run the tests.

3. Convert `Age` to numeric and handle missing values
   - Print it and run the tests.

4. Convert `Salary` to numeric and replace known placeholders (`unknown`, `n/a`) with NaN
   - print it and run the tests.

5. Fill missing numeric values (use `fillna`).  Fill `Age` which the mean and `Salary` with the median
   - Print it and run the tests

6. Convert `Hire Date` to `datetime`
   - Print it and run the tests

7. Strip extra whitespace and standardize `Name` and `Department` as uppercase
   - Print it and run the tests


---

### **Step 2: Submit Your Assignment on GitHub**  

**Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment3` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment3` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**.  

---
