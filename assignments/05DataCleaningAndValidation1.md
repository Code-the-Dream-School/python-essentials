## Lesson 5 Assignment — Data Cleaning and Validation I
### Data Cleaning and Validation with Pandas

### **Objective:**
This assignment focuses on exploring fundamental data cleaning and validation techniques using the Pandas library in Python. You will learn how to handle missing data, transform data types, remove duplicates, manage outliers, standardize data, encode categorical variables, and validate data ranges.

This assignment is to be created in a Kaggle notebook, as you did for Assignment 4.  This time, create a notebook called CTD_Assignment_5 for code as described below.

### **Tasks:**

### **Task 1: Handling Missing Data**

1. **Create a DataFrame using the provided data:**
   - The DataFrame contains columns for 'Name', 'Age', 'Salary', 'Join_Date', and 'City', with some missing values.
   - Print the original DataFrame.
  
Here's a summary of what the DataFrame looks like to help you get started: 

```python
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, None, 35, 40, 30],
    'Salary': [50000, 60000, None, 80000, 55000],
    'Join_Date': ['2020-01-01', None, '2020-03-15', '2020-04-20', None],
    'City': ['New York', 'Los Angeles', 'Chicago', None, 'Miami']
}
df = pd.DataFrame(data)
```

You can find the Kaggle data set at https://kaggle.com/datasets/9b958a131430c339b0f13e5851bcfa7654e217f0ce3db66abdb1a26ab59c059d. While logged in you should be able to click "Code" and create a notebook out of this data.

After you do this you can use the following to load the CSV into a data frame.
```Python
df = pd.read_csv('/kaggle/input/code-the-dream-lesson-5/fake_data.csv')
```
2. **Perform the following operations on  new DataFrames:**
   - **Remove rows with missing values** using the `dropna()` method and print the updated DataFrame.
   - **Replace missing values** using the `fillna()` method:
     - Replace missing 'Name' values with `'Unknown'`.
     - Replace missing 'Age' values with the **mean** of the 'Age' column.
     - Replace missing 'Salary' values with the **median** of the 'Salary' column.
     - Replace missing 'Join_Date' values with `'2020-01-01'`.
   - Print the updated DataFrame after replacing missing values.

### **Task 2: Data Transformation**
1. **Convert Data Types:**
   - Convert the 'Age' column to **integer** type using `astype(int)`.
   - Convert the 'Join_Date' column to **datetime** format using `pd.to_datetime()`.
   - Print the updated DataFrame.

**Hint:** Use `errors='coerce'` in `pd.to_datetime()` to handle invalid dates gracefully.

### **Task 3: Removing Duplicates**
1. **Identify and remove duplicate records:**
   - Use the `duplicated()` method to identify duplicate rows in the DataFrame.
   - Use the `drop_duplicates()` method to remove duplicate rows.
   - Print the updated DataFrame.
  
**Hint:** By default, `drop_duplicates()` keeps the first occurrence of each duplicate row. Use the `keep` parameter to change this behavior if needed.

### **Task 4: Handling Outliers**
1. **Identify and replace outliers in the 'Age' column:**
   - Consider outliers as values greater than 100 or less than 0.
   - Replace outliers with the **median** of the 'Age' column.
   - Print the updated DataFrame after handling outliers.

**Hint:** Outliers can also be identified using statistical methods like the Interquartile Range (IQR) or Z-scores.

### **Task 5: Standardizing Data**
1. **Standardize the 'Name' column:**
   - Convert all names to lowercase and trim any leading or trailing whitespace using `str.lower()` and `str.strip()`.
   - Print the updated DataFrame.

2. **Standardize inconsistent entries in the 'City' column:**
   - Replace variations like 'new york' with 'New York' and 'la' or 'los angeles' with 'Los Angeles'.
   - Print the updated DataFrame.

### **Task 7: Validating Data Ranges**
1. **Ensure the 'Age' column contains values within the valid range (18 to 65):**
   - Replace invalid ages (less than 18 or greater than 65) with `NaN`.
   - Fill the missing values with the **median** of the 'Age' column.
   - Print the updated DataFrame.

**Hint:** Validating data ranges ensures that your data is consistent and suitable for analysis or modeling.

### **Submit the Notebook for Your Assignment**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy the public URL to your clipboard.

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
