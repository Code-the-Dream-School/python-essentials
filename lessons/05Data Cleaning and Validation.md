
## Lesson 05 — Data Cleaning and Validation I

**Lesson Overview**

**Learning objective:** Students will learn essential data cleaning and transformation techniques in Pandas, including handling missing values, outliers, and duplicates. They will also use pivot tables, the `apply()` method, and column-wise operations to reshape and enrich datasets.


### Topics

1. **Pivot Tables**: A way to present summary data.
2. **Transforming DataFrames with apply()**: A flexible way to create new columns by combining column entries from existing columns.
3. **Intro to Data Cleaning**: Identifying dirty data; understanding standardization, outliers, deduplication, and validation. 
4. **Handling Missing Data**: Removing rows with `dropna()`, replacing values with `fillna()`. 
5. **Data Transformation**: Converting data types, reformatting dates, **feature engineering**, **data discretization**. 
6. **Removing Duplicates**: Identifying and removing duplicate records.
7. **Removing Outliers**: Identify and removing outlying records
---

## 5.1 Pivot Tables.

As usual, run these examples in the Python interactive shell of your `python_homework` terminal session.

Consider the following case. Acme Inc. has 3 sales employees and 2 regions.  The employees each report the revenue they got from sales of each of the products in each of the regions.  These reports are probably kept in a database, but for our purposes, they look like this:
```python
include pandas as pd
data = [{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 11000}, \
{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 5500}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2345}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003}, \
{'Employee': 'Smith', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 110012}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'East', 'Revenue': 9002}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 15500}, \
{'Employee': 'Garcia', 'Product': 'Widget', 'Region': 'West', 'Revenue': 6007}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 42003}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 160012}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 16500}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2458}]
sales = pd.DataFrame(data)
print(sales)
```
Ok, all the information is here, but it is not organized as the CFO would like.  You have already learned one way to summarize the data, using groupby().  Another is to use pivot tables.  Here are three examples:

```python
sales_pivot1 = pd.pivot_table(sales,index=['Product','Region'],values=['Revenue'],aggfunc='sum',fill_value=0)
print(sales_pivot1)
# This creates a two level index to show sales by product and region. The revenue values are summed for each product and region.
sales_pivot2 = pd.pivot_table(sales,index='Product',values='Revenue',columns='Region', aggfunc='sum',fill_value=0)
print(sales_pivot2)
# The result here is similar, but instead of a two level index, you have columns to give sales by region.
sales_pivot3 = pd.pivot_table(sales,index='Product',values='Revenue',columns=['Region','Employee'], aggfunc='sum',fill_value=0)
print(sales_pivot3)
# By adding the employee column, you get these revenue numbers broken down by employee.  The fill value is used when there is no corresponding entry.
```
By gaining familiarity with pivot tables, you can present data in various ways that make it easy to show the business picture.

## 5.2 Using apply()

You have already learned several ways to generate a new column from an existing one.  Suppose, however, that you want to combine information from several columns.  For example, you could do the following:
```python
sales_pivot2['Total'] = sales_pivot2['East'] + sales_pivot2['West'] # adding two columns to make a new one
print(sales_pivot2)
per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Percentage'] = [0.12, 0.09, 0.1]
per_employee_sales['Commission'] = per_employee_sales['Revenue'] * per_employee_sales['Commission Percentage']
print(per_employee_sales)
```
Ok, so far so good.  But suppose the combination rules are a little more complicated.  Consider this case:
```python
per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Plan'] = ['A', 'A', 'B']
```
Sales employees on commission plan A get $1000 for the first 10000 in revenue, and 5% for revenue over 10000.  Everyone else gets $1400 for the first 10000 in revenue, but 4% for revenue over 10000.  All employees get zip if they don't get at least 10000 in revenue. You use apply(), and you specify `axis=1` to request the entire row.  You pass a function to apply(), and the function is called once per row.  As follows:
```python
def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)

per_employee_sales['Commission'] = per_employee_sales.apply(calculate_commission, axis=1)
print(per_employee_sales)
```

## 5.3 What is Data Cleaning?

Data is often dirty.  Values may be missing, or duplicated, or incorrectly formatted, or have values that are not plausible or manageable by data analysis.  The following optional [video](https://www.youtube.com/watch?v=WpX2F2BS3Qc) expains the concepts.  The main idea is garbage-in, garbage-out.  Any analysis you do on data that is partly incorrect may be invalid.  Data cleaning involves the following procedures:

- Standardization.  For example, you want to represent dates and phone numbers in a standard way.
- Addressing outliers.  These are values that appear improbable and were likely entered in error.
- Deduplication.
- Addressing missing values.
- Validation.

You will learn various technical approaches to each of these.

### Standardization

You can check, for example, that email addresses are of a valid format.  Suppose some are not.  You can either flag the rows for manual correction, or discard the rowss, or attempt to reformat the addresses to correct the problem, or derive the correct addresses from other information in the row or perhaps in a separate dataset.  For US phone numbers, you could check that each is a string of 10 numeric characters.

### Addressing Outliers

Sometimes outliers are easy to identify.  If a person's age is negative, or greater than 120, this is an outlier.  But in other cases, it might not be so clear.  For example, if you discarded outliers for daily rainfall in a region, you could end up discarding all flood events, which are important records that are needed for the analysis.

### Deduplication

Deduplication is pretty easy if the rows are exactly the same.  But, if one of the values in the row is a little bit different, it may not be as clear.  Perhaps you have access to a reliable key, such as a known phone number or email address.

### Addressing missing values

You can throw away the rows with missing information ... but other parts of the record may have valuable information.

You can substitute a plausible value ... but this distorts the data.  For example, if the data contains a person's net worth, you could substitute the mean value for that column, but actually most people don't have nearly the 'average' net worth.  You could substitute the median value instead, but again, most people have incomes that differ from the median by quite a bit.

Each automated change to clean the data involves a tradeoff.  You should always archive the original data, in case cleaning introduces distortions.

### Validation

This is a process to check that the cleaned data is in fact correct.  For example, for information about a person, you might want to ask the person if the stored information is correct.


## 5.4 Handling Missing Data

### Overview

Missing data is common in datasets and can significantly affect the outcome of analyses if not handled properly. In Pandas, there are methods to identify and handle missing data, either by removing rows or by filling in the missing values. Correctly managing missing data is crucial for ensuring accurate results.

### Key Methods

- `isnull()`: Find the rows where data is missing.
- `dropna()`: Removes rows or columns with missing data.
- `fillna()`: Replaces missing values with specified values.

### Why Handle Missing Data?

- Ensures accurate calculations and visualizations.
- Prevents runtime errors during analysis.
- Allows consistent dataset formatting.

### Example: Using `isnull()`, `dropna()` and `fillna()`

**For this and all examples below, you should run the code within the Python interactive shell of your python_homework VSCode terminal.**

```python
import pandas as pd

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print(df_missing)
# Remove rows with missing data
df_dropped = df.dropna()
print(df_dropped)

# Replace missing data with default values
df_filled = df.fillna({'Age': 0, 'Score': df['Score'].mean()})
print(df_filled)
```

**Explanation:**
`df.isnull().any(axis=1)` finds the rows that have null or NaN values.  The `axis=1` is needed to specify rows.

`dropna()` removes any row that contains a `None` (missing) value. This can remove quite a lot of data, especially if you have a lot of columns.

`fillna()` is used to replace missing values. In this case, the `Age` column's missing values are replaced with 0, and the `Score` column's missing values are filled with the mean of the existing scores. This can cause issues if the values you are replacing become outliers.

## 5.5 Data Transformation

### Overview

Data transformation is essential for ensuring that all data conforms to the correct format and type, which makes it easier to manipulate and analyze. This includes tasks like converting strings to numeric values, reformatting date strings into datetime objects, **creating new features** (feature engineering), and **discretizing continuous variables**.

### Key Tasks

- Converting data types (e.g., strings to integers).
- Reformatting date strings into datetime objects.
- **Creating new features:** 
    - Combining existing features (e.g., `Age` and `YearsOfExperience` to create `AgeGroup`).
    - Extracting features from existing ones (e.g., extracting `Year` and `Month` from a `Date` column).
    - Generating interaction features (e.g., multiplying two features).
- **Data Discretization:** 
    - Binning continuous variables into discrete categories (e.g., age ranges, income brackets).
    - Using techniques like `pd.cut()` or `pd.qcut()`.

### Why Transform Data?

- Prevents errors due to mismatched data types.
- Simplifies operations such as comparisons and calculations.
- Ensures uniformity in dataset representation.
- Improves model performance in machine learning tasks.

### Example: Converting Data Types and Reformatting Dates

```python
import pandas as pd

# Sample DataFrame with mixed data types
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Age' column to integers
df['Age'] = df['Age'].astype(int)

# Convert 'JoinDate' column to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)  # Verify data types
print(df)
```
In addition you can use the Series map() method to change items in a column.

```python
import pandas as pd

# Sample DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Location' abbreviations into full names

df['Location'] = df['Location'].map({'LA': 'Los Angeles', 'NY': "New York"})
print(df)
```

The problem with the code above is that if the value in the 'Location' column is not either 'LA' or 'NY', it is converted to `NaN`.  Suppose you want to preserve the existing value in this case. You'd use the replace() method instead:

```python
df['Location'] = df['Location'].replace({'LA': 'Los Angeles', 'NY': "New York"})
```

Here is another case.  Suppose we have a list of people's phone numbers, but they are not in standard format.  We can attempt to clean this up in this way:

```python
import pandas as pd
data = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'], 'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None
    
df['Correct Phone'] = df['Correct Phone'].map(fix_phone)
print(df)
```
In the code above, the 'Phone' column is preserved, in case there is useful information, but the 'Correct Phone' column is created, with a best effort at reformatting the phone numbers.  Note that the logic did not fit in a lambda, so a function was declared to pass to map().

Finally we can use built in numpy functions in order to change all of the data in a data frame by following a function
```python

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
	'Age': [20, 22, 43]}

df = pd.DataFrame(data)

# Increase the age by 1 as a new year has passed
df['Age'] = df['Age'] + 1
print(df)
```


For **Data Discretization** we have to use the more complicated pandas.cut() function. This will allow us to automatically split data into a series of equal sized bins.

```python
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]}
df = pd.DataFrame(data)

# Convert grade into three catagories, "bad", "okay", "great"

df['Grade'] = pd.cut(df['Grade'], 3, labels = ["bad", "okay", "great"])
print(df)
```

**Explanation:**

`astype(int)` converts the `Age` column, originally stored as strings, into integers.
`pd.to_datetime()` converts the `JoinDate` column into Python’s datetime objects for easier date manipulation and comparison.
`pd.cut()` allows us to create bins for data and provide data discretization

---

## 5.6 Removing Duplicates

### Overview

Duplicate records can inflate metrics and skew results. Removing duplicates ensures that each record is unique, which improves the reliability of analyses. Pandas provides the `drop_duplicates()` method to identify and remove duplicate rows.

### Key Method

- `drop_duplicates()`: Removes duplicate rows based on one or more columns.

### Why Remove Duplicates?

- Prevents redundant information in analysis.
- Improves data quality and storage efficiency.
- Ensures unique data for accurate insights.

### Example: Using `drop_duplicates()`

```python
import pandas as pd

# Sample DataFrame with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 32],
        'Score': [85, 92, 85, 76]}
df = pd.DataFrame(data)

# Identify and remove duplicates
df_cleaned = df.drop_duplicates()
print(df_cleaned)

# Remove duplicates based on 'Name' column
df_cleaned_by_name = df.drop_duplicates(subset='Name')
print(df_cleaned_by_name)
```

**Explanation:**

`drop_duplicates()` removes rows where the entire record is a duplicate of another.
`drop_duplicates(subset='Name')` removes rows where the `Name` column is duplicated, keeping only the first occurrence of each name.

---

## **5.7 Handling Outliers**

### **Overview**
Outliers are extreme values that deviate significantly from other observations and can bias statistical calculations.

### **Common Approach:**
- Replace outliers with statistical measures like the median.

### **Code Example:**

(You don't need to run this one, as the DataFrame is not provided.)

```python
# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

print("DataFrame after handling outliers:")
print(df)
```

### **Explanation:**
- Outliers in the `Age` column that are greater than 100 or less than 0 are replaced by the median value of the `Age` column.

---



### Example

**Check for Understanding**

Which method removes rows with missing values?

A) `fillna()`
B) `dropna()`
C) `remove_missing()`
D) `replace_na()`

<details>
<summary>Answer</summary>
Answer: B
</details>

How do you convert a column of strings to integers?

A) `pd.to_int(column)`
B) `df['column'].convert(int)`
C) `df['column'].astype(int)`
D) `df['column'].to_int()`

<details>

<summary>Answer</summary>

**Answer**: C

</details>


Which method is used to remove duplicate rows in Pandas?

A) `remove_duplicates()`
B) `drop_duplicates()`
C) `find_duplicates()`
D) `remove_redundant()`

<details>

<summary>Answer</summary>

**Answer**: B

</details>

**Summary**

In this lesson, you’ve learned:

* How to use pivot tables for improved data presentation.
* How to use apply() on a DataFrame to generate a new column.
* Concepts in data cleaning.
* How to handle missing data using `isnull()`, `dropna()` and `fillna()`.
* How to transform data by converting data types, reformatting dates, and discretizing continuous variables.
* How to identify and remove duplicate records with `drop_duplicates()`.
* How to remove outliers using statistical methods.

By applying these techniques, you can clean and validate your datasets for accurate and effective analysis. For further exploration, refer to the Pandas Documentation and Python's official documentation.
