## Lesson 4 Assignment — Data Wrangling and Manipulation
### Advanced Data Wrangling and Aggregation with Pandas

### **Objective:**
The purpose of this assignment is to deepen your understanding of data wrangling and aggregation using the Pandas library in Python. You will work with sample DataFrames to perform various operations such as filtering, handling missing values, merging, sorting, and transforming.

### **Setup**

The assignments up to this one have required you to create `.py` files and to submit them by creating pull requests for your python_homework repository.  For this assignment, you create a Jupyter notebook file.  Jupyter notebooks are a way to do data presentation and analysis, using Python code.  A notebook is comprised of a sequence of cells, which come in two kinds: Markdown cells, for putting in the text you want to show, and code cells, where you put your Python code.

With a little setup, you can create Jupyter notebooks in VSCode, and submit them to GitHub.  However, GitHub is not a friendly environment for collaboration on notebooks.  Your reviewer wants to see the notebooks, to run them, and to give you comments in context.  For that purpose, we use [https://kaggle.com].  That site also has an interesting collection of data sets you can use for practice in data analysis and presentation.  Connect to the site now and register, so that you have an account.

### **Tasks:**

### **Task 1: Data Selection**
1. **On the Kaggle site, click on the plus button in the upper left, and create a notebook called CTD_Assignment_4.**  It comes up with a code cell already present.  Leave that one alone, and click on the plus code button to add another cell.  You add the code for this assignment to the cell.  As you complete each of the following tasks, run the cell to make sure your code works.  You run the cell by clicking on the arrow at the top left of the cell.  Again, put comments in your code to indicate where you have completed each task.

2. **Create DataFrames `df1`, `df2`, and `df3` using the provided sample data(feel free to change the values):**
   - `df1` contains names, ages, and salaries of five employees.
   - `df2` contains names, ages, and salaries of five other employees.
   - Display each DataFrame.
   
```
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}
```

```
data2 = {
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
}

data3 = {
    'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
    'Age': [17, 93, 12, 57, 106],
    'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
}
```
Print the resulting dataframes. 

3. **Perform the following selection operations on `df1`:**
   - Select the 'Name' column, and print the result.
   - Select both 'Name' and 'Salary' columns, and print the result.
   - Slice the first three rows using integer-based indexing (`iloc`), and print the result.

### **Task 2: Data Aggregation**
1. **Group `df1` by 'Age' and aggregate the 'Salary' column:**
   - Calculate the mean, sum, and count of the salary for each age group.
   - Display the aggregated results.

### **Task 3: Merging and Joining DataFrames**
1. **Merge `df1` and `df3` into `df_1_3_merged` on the 'Name' column:**
   - Use an outer join to combine the two DataFrames and handle any missing data.
   - Use the suffixes `_df1` and `_df2` to differentiate columns from each DataFrame. (You specify `suffixes=['_left','_right']` on the call to merge.)
   - Display the result with print(). 
   - We see that the 'Salary' column has `NaN` values.  Transform this column to replace `NaN` with the starting salary of 15000.  Hint: fillna() can be used on a Series.
   - Also, transform the 'Favorite Color' column to replace `NaN` values with 'yellow'.
   - Reset the index on the merged DataFrame.
   - Display the result.
   - We have `NaN` for some of the entries in the 'Age_left' column.  For other rows, the `NaN` value is in the 'Age_right' column.  We want to create a new `Age` column, using the values from 'Age_left' if they are not `NaN`, and from 'Age_right' otherwise.  We'll use np.where().  As this is a new technique, the answer is as follows:
       ```python
       import numpy as np
       df_1_3_merged['Age'] = np.where(df_1_3_merged['Age_left'].notna(),df_1_3_merged['Age_left'], df_1_3_merged['Age_right'])
       # This works like a ternary expression.  If the expression passed to np.where is True, you get the left value, otherwise the right value.
       ```
   - Display the result.
   - Drop the 'Age_left' and 'Age_right' columns and display the result.

2. **Use the Join Method:**
   - Create new DataFrames df1_b and df3_b.  In these, set 'Name' as the index.  Do not use `inplace=True`.
   - Join the DataFrames with outer join logic and display the result.

### **Task 4: Filtering Rows Based on Conditions**
1. **Filter rows in `df1` where 'Age' is greater than 30:**
   - Display the filtered rows.

### **Task 5: Sorting Data**
1. **Sort `df1` by the 'Salary' column in descending order:**
   - Display the sorted DataFrame.

### **Task 6: Renaming Columns**
1. **Rename columns in `df1`:**
   - Rename 'Age' to 'Employee Age' and 'Salary' to 'Employee Salary'.  Do not use `inplace=True`, because then you wouldn't be able to do Task 9.
   - Display the DataFrame with the renamed columns.

### **Task 7: Data Transformation**
1. **Apply a transformation to the 'Salary' column in `df1`:**
   - Increase the salary by 10% for each employee.
   - Display the updated DataFrame.

### **Task 8: Concatenating DataFrames**
1. **Concatenate `df1` and `df2` to add the rows of `df2` to the end of `df1`**
   - Use `ignore_index=True` to reset the index.
   - Display the result.

### **Task 9: Data Wrangling a Kaggle Dataset**

Kaggle has some nice datasets you can use in exercises.  These are `csv` files.  We are going to do some data wrangling on one of those provided files. For this task, we are going to find the international football teams that are especially bad on defense.
- Open another Kaggle window in your browser.
- On the upper right of your notebook, click on 'Add Input'.  Click on the 'Datasets' button.  Then do a search on 'international football results'.  You should see one from Mart Jürisoo.  Click on the plus sign next to that one.  That adds the dataset to your notebook, so that you can read the CSV files.
- Create a new code cell in your notebook for the following steps.
- You need to find the available CSV file path names, a little tricky in Kaggle. Add the following code, and then run your cell:
    ```python
    import pandas as pd
    import os
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
    ```
- This will list, among others, the path `/kaggle/input/international-football-results-from-1872-to-2017/results.csv`.  This is the one you want.  Read it into a DataFrame called football_results.
- Print the first 5 lines of this file.
- All the entries have a home team and an away team.  This is kind of clumsy for us, because we want results for each team whether they were home or away.  So, we'll create a new DataFrame that organizes the in that way.  First, create a DataFrame called results_1.  You select the following columns from football_results: 'home_team','away_team','home_score','away_score',  and 'date'.  Print out the first 5 lines.
- Next, create a DataFrame called results_2 from results_1.  You rename the column for 'home_team' to 'team', for 'away_team' to 'opponent', for 'home_score' to 'points_for', and for 'away_score' to 'points against'.  Do not use `inplace=True`.  This dataset gives all the entries for the home teams.  Print out the first 5 lines.
- Next, create a DataFrame called results_3 from results_1.  This also renames the columns, but now the rename is: 'away_team' becomes 'team', 'home_team' becomes 'opponent', 'away_score' becomes 'points_for', and 'home_score' becomes 'points_against'.  This dataset gives all the entries for the away teams.  Print out the first 5 lines.
- Concatenate the results, resetting the index.  Store the result in football_results.  Print out the first 5 lines.  Now we have all the entries per team.
- Do a `groupby()` on 'team'.  Get the mean() of the 'points_against' column.  Store the result (it is a Series) in the variable points_against.
- Sort points_against so the values are descending.  Print out the first 10 lines.  These are the teams that are very bad on defense.

### **Task 10: More Data Wrangling for Football Results**

This time, you'll have to figure out the steps.  Starting with the football_results DataFrame you created in Task 10, print out the most recent 10 games for Tunisia.  Remember to sort these so that you get the right games.


### **Submit the Notebook for Your Assignment**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy the public URL to your clipboard.

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
