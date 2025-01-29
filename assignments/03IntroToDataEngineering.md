## Lesson 3 Assignment — Intro to Data Engineering
### Data Analysis and Manipulation with Pandas

### **Objective:**
In this assignment, you will explore the basic functionalities of the Pandas library in Python, including creating, manipulating, inspecting, and analyzing data using various DataFrame methods. The goal is to understand how to handle data efficiently and perform essential operations to inspect and analyze datasets.

### **Tasks:**

### **Task 1: Introduction to Pandas - Creating and Manipulating DataFrames**
1. **Create a DataFrame from a dictionary:**
   - Use a dictionary containing the following data:
     - `Name`: ['Alice', 'Bob', 'Charlie']
     - `Age`: [25, 30, 35]
     - `City`: ['New York', 'Los Angeles', 'Chicago']
   - Convert the dictionary into a DataFrame using Pandas.
   - Print the DataFrame to verify its creation.

2. **Add a new column:**
   - Add a column called `Salary` with values `[70000, 80000, 90000]`.
   - Print the updated DataFrame.

3. **Modify an existing column:**
   - Increment the `Age` column by 1 for each entry.
   - Print the modified DataFrame to verify the changes.
   - 
4. **Save the DataFrame as a CSV file:**
   - Save the DataFrame to a file named employees.csv using ```to_csv()```.
     

### **Task 2: Loading Data from CSV, JSON, and Dictionaries**
1. **Read data from a CSV file:**
   - Create a sample CSV file using the DataFrame from Task 1.
   - Load the CSV file into a new DataFrame and print it.

2. **Read data from a JSON file:**
   - Create a JSON file (additional_employees.json) with the following data:
     
```

  {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
  {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}

```
   - Load this JSON file into a new DataFrame using pd.read_json().
   - Print the DataFrame to verify it loaded correctly


3. **Combine DataFrames:**
   - Append the data from the JSOn file to the DataFrame Loaded from the CSV file.
   - Print the combined Dataframe

### **Task 3: Data Inspection - Using Head, Tail, and Info Methods**
1. **Use the `head()` method:**
   - Print the first 5 rows of the original dictionary DataFrame using the `head()` method.

2. **Use the `tail()` method:**
   - Print the last 2 rows of the original dictionary DataFrame using the `tail(2)` method.

3. **Use the `info()` method:**
   - Print a concise summary of the DataFrame using the `info()` method to understand the data types and non-null counts.

### **Task 4: Additional Data Inspection and Analysis**
1. **Determine the shape of the DataFrame:**
   - Use the `shape` attribute to print the number of rows and columns in the original DataFrame.

2. **Use the `describe()` method:**
   - Print a statistical summary of the numeric columns in the DataFrame, including count, mean, standard deviation, min, max, and quartiles.

3. **Calculate the correlation matrix:**
   - Use the `corr()` method to print the correlation matrix of the numeric columns, indicating how the columns are related to each other.

### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Upload Your Assignment**  
- Go to your `python-essentials` GitHub repository.
- Click the **Add file** dropdown and select **Create new file**.
- Create a folder for this lesson by typing the lesson name followed by a `/` (i.e., `lesson-03/`)
- Name the file by typing the file name. (i.e., `lesson-03/assignment.py` or `lesson-03/assignment.ipynb` for a Jupyter Notebook).  
- Paste your code into the file OR click **Upload files** and add your `.py` or `.ipynb` file.  
- Click **Commit new file** to save your work.  

#### **3️⃣ Submit Your GitHub Link**  
- Open your repository and navigate to the `lesson-03` folder.  
- Copy the URL of the folder (e.g., `https://github.com/your-username/python-class-your-name/tree/main/lesson-03`).  
- Paste the URL into the **assignment submission form**.  

---

## **✅ Submission Checklist**  
Before submitting, make sure:  
- [ ] Your repository follows the format `python-class-your-name`.  
- [ ] Your assignment is inside a `lesson-03` folder.  
- [ ] You've uploaded your `.py` or `.ipynb` file.  
- [ ] You’ve copied and submitted the correct GitHub folder URL.  

---
