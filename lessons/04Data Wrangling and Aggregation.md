
# **Lesson 04 — Data Wrangling and Aggregation**

## **Lesson Overview**
**Learning objective:** Students will learn to manipulate, summarize, and combine datasets in Pandas using selection, aggregation, merging, and transformation methods. They will practice accessing specific data, performing group-level calculations, and combining data from multiple sources.


### **Topics:**
1. Pandas Review (Optional): Recap of Series, DataFrames, and key methods from Lesson 3.
2. Data Selection: Selecting subsets with `.loc[]`, `.iloc[]`, `.at[]`, and `.iat[]`; filtering rows by conditions; applying string methods.
3. Data Aggregation: Grouping data with `groupby()`; applying functions like `sum()`, `mean()`, and `count()`; using `agg()` for multiple aggregations.
4. Merging and Joining: Combining DataFrames with `merge()` and `join()`; inner, outer, left, and right joins; joining on one or multiple keys.
5. Data Transformation: Adding, updating, and deleting columns; using operators, Series methods, `map()`, and NumPy functions for transformation.
6. Utility Methods: Renaming columns, setting or resetting index, and sorting data.
---

## **4.1 Pandas Review & Deep Dive** *(Optional)*

Last week, we introduced Pandas, a powerful tool for data analysis. If you want a refresher on key Pandas concepts, **[listen to this NotebookLM-generated podcast](https://youtu.be/T46zVBxHrjc) reviewing what we learned last week**. 

*Note: The podcast references two sources, linked below.*

  * (PDF) [Introduction to Pandas](https://github.com/Code-the-Dream-School/python-essentials/blob/ff583aac6befdb1e008b4d149527bc0dd5c437ef/lessons/resources/Pandas%201%20PDF.pdf)
  * (Slide Deck) [Pandas for Dummies](https://www.qrious.co.nz/hubfs/pandas4dummies.pdf)

## **4.2 Data Selection**

### **Overview**
Indexing and slicing allow you to extract specific rows or columns from a DataFrame, making it easier to analyze subsets of your data.

### **Key Methods:**
- `.loc[]`: Select rows and columns by labels.
- `.iloc[]`: Select rows and columns by integer position.
- `.at[]`: Access a specific cell by label.
- `.iat[]`: Access a specific cell by position.

### **Why Use Data Selection?**
Data selection helps you:
- Filter relevant data for analysis.
- Access specific values or ranges for visualization or calculation.
- Preprocess data by selecting subsets of interest.

**You should run all of the following code examples within the Python interactive shell.**  Start VSCode from within your `python_homework` directory, start a terminal within VSCode, and enter the `python` command to start the shell.

### **Example: Using `.loc[]` and `.iloc[]`**
```python
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'Score': [85, 92, 88, 76]}
df = pd.DataFrame(data)

# Select the 'Name' column
print(df['Name'])

# Select rows and specific columns
print(df.loc[0:2, ['Name', 'Age']])

# Select rows by position
print(df.iloc[:2])  # First two rows
```
## **Explanation:**
`.loc[]` is used for label-based indexing. Here, df.loc[0:2, ['Name', 'Age']] selects rows 0 to 2 and the 'Name' and 'Age' columns.
`.iloc[]` is used for position-based indexing. df.iloc[:2] selects the first two rows.

This is slicing, similar to the slicing of lists described in lesson 2.  There are some differences however. The indices for df, in this case, are 0 through 3.

```python
print(df.loc[0:2])  # This prints the first 3 rows! It starts with the row with index 0 and continues up to and including the row with index 2.
print(df.iloc[:2]) # This prints the first 2 rows only.  iloc[] works like list slicing.  It does not include the row with index 2.
print(df.loc[[0,2]]) # This prints row 0 and row 2.  You specify a list of the rows you want.  You can't do this with lists!
```
In each of the cases above, what is returned is a new DataFrame that is a subset of the old one.

One can also specify a filter.  For example:

```python
print(df[df['Age'] > 24])
# print(df[df['Age'] > 24 and df['Score'] >=88])         Doesn't work!  'and' is not a valid operator for Series!
print(df[(df['Age'] > 24) & (df['Score'] >=88)])        # This one does work! It does the boolean AND of corresponding series elements.
# print(df["a" in df['Name']])                          Doesn't work!  The "in" operator doesn't work for Series!
print(df[df['Name'].str.contains("a")])                 # This does work!  
# There are a bunch of useful str functions for Series.  While we're at it:
# df['Name'] = df['Name'].upper()                       Doesn't work!!
df['Name'] = df['Name'].str.upper()                     # Does work! 
print(df)
```


## **4.3 Data Aggregation**

### **Overview**
Aggregating data involves summarizing it by groups, enabling insights at a higher level (e.g., total sales by region, average score by category).

### **Key Method:**
- `groupby()`: Groups data by one or more columns.
- Aggregation functions: `sum()`, `mean()`, `count()`, etc.

### **Why Use Aggregation?**
Aggregation simplifies data analysis by:
- Summarizing patterns across categories.
- Providing key metrics like totals, averages, and counts.
- Reducing data complexity.

### **Example: Using `groupby()`**
```python
# Group data by a column and calculate the sum
data = {'Category': ['A', 'B', 'A', 'B', 'C'],
        'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum
grouped = df.groupby('Category').sum()
print(grouped) # grouped is another DataFrame with summary data

# Calculate the mean for each group
mean_values = df.groupby('Category')['Values'].mean()
print(mean_values)
```
## Explanation: 
- **`df.groupby('Category').sum()`** groups the data by the 'Category' column and calculates the sum of 'Values' within each category.
- **`df.groupby('Category')['Values'].mean()`** calculates the mean of 'Values' for each category.

---

### **Advanced Aggregation**

You can apply multiple aggregation functions at once by using `agg()`. This allows you to calculate various summary statistics for each group.

#### Example: Applying Multiple Aggregations

```python
import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'C'],
        'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Group by 'Category' and apply multiple aggregation functions
result = df.groupby('Category').agg({'Values': ['sum', 'mean', 'count']})
print(result)
```

## **Explanation:**

`sum()` calculates the total sum of values for each category.
`mean()` calculates the average value for each category.
`count()` counts the number of non-null entries for each category

Note: For a given agg() invocation on a column, you can specify one or several aggregation functions:

```python
result1 = df.groupby('Category').agg({'Values': 'sum'})
# or
result2 = df.groupby('Category').agg({'Values': ['sum', 'mean', 'count']})
```
If you print out result1 and result2, you'll see that they look different.  The result2 DataFrame has column headers with several rows, because 3 columns are needed for Values aggregation, one for some, one for mean, and one for count.  The column names in this case are tuples, such as `("Values","sum").

In the result1 case, you just have one column for the sum of values, and the column name is "Values".  The difference hangs on whether you specify a single aggregation function or a list.

## **4.4 Merging and Joining**

### **Overview**
Combine multiple DataFrames using shared keys (columns or indices). 

### **Key Methods:**
- `merge()`: Combines DataFrames on common columns.
- `join()`: Combines DataFrames based on their indices.

### **Why Use Merging and Joining?**
- Combine related datasets for comprehensive analysis.
- Handle data stored across multiple sources.
- Maintain relationships between data records.

### **Example: Using `merge()`**
```python
# Sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 92, 88]})

# Merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)  # Inner merge
```

The merged DataFrame has the columns from both DataFrames.  In this case the key is the 'ID' column.  If those match up, the rows of the merged DataFrame will have both 'Name' and 'Score' columns.

Suppose that the two DataFrames also both have an 'Age' column.  You end up with an `Age_x` and an `Age_y` columns, where the renaming is done to prevent collision.  There are ways to choose which one you want to keep.

This is an inner merge.  That means you get only the rows where the ID values match.  One could specify a `how` value of 'left', 'right', or 'outer'.  'left' means include all rows from the left DataFrame, along with matching rows from the right DataFrame.  'right' means the converse.  And 'outer' means include all rows, matching up the ones for which the 'ID' is the same.  When using 'left', 'right', or 'outer', you get `NaN` values in the columns to be added for rows that don't match up.
### Merging on Multiple Columns

Sometimes you need to merge two DataFrames based on multiple columns. This is useful when you have composite keys or want to match on more than one condition.

```python
import pandas as pd

# Sample DataFrames

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Score': [85, 92, 88]
})

# Merge on both 'ID' and 'Date'
merged_df = pd.merge(df1, df2, on=['ID', 'Date'], how='inner')
print(merged_df)
```
In this example:

Merging on both 'ID' and 'Date': This allows you to ensure that the rows are only merged when both conditions match, i.e., the same ID and the same Date.
how='inner': This ensures that only the rows with matching values in both DataFrames are included in the result.

## **Explanation:** 
The merge() function combines two DataFrames based on a common column. Here, it's merging df1 and df2 on the 'ID' column using an inner join, meaning only rows with matching 'ID' values from both DataFrames will appear in the result.  You can also use the join() function.  This matches on index values, instead of the values in one or several key columns.

### **Example: Using `join()`**
```python
# Join DataFrames by index
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[1, 2, 3])
df2 = pd.DataFrame({'Score': [85, 92, 88]}, index=[1, 2, 4])

joined_df = df1.join(df2, how='outer')
print(joined_df)
```

## **Data Transformation**

While one can do transformation of the DataFrame as a whole, for the moment we will focus on approaches that do it one column at a time.  You can add, replace, or delete a column of a DataFrame at any time.

```python
joined_df['bogus']=['x','y','z','w'] # adds a column
print(joined_df)
joined_df['bogus']=joined_df['bogus'] + "_value"  # replaces a column
print(joined_df)
joined_df.drop('bogus', axis=1, inplace=True) # deletes the column.  You need axis=1 to identify that the drop is for a column, not a row
print(joined_df)
```

Look carefully at the case where the column is replaced.  `joined_df['bogus']` returns a view of the column, which is a Series.  You don't write to that directly.  You create a new column, transforming the existing value.  In this case, "_value" is concatenated to each of the values in the original view.  Then, you replace the 'bogus' column with the new column.

You can transform a Series in several ways.
- You can use an operator, as in the above example.  Of course, you can't raise a string to a power of 2, or anything like that, so the type of the entry is important.
- You can use a Series method.  One important example is the map() method, but there are others, such as astype().
- You can use a NumPy function that can operate on a Series.  
Let's look at an example of each:

```python
import numpy
data = {'Name': ['A','B','C'],'Value':[1,2,3]}
new_df = pd.DataFrame(data)
print(new_df)
new_df['Value'] = new_df['Value'] ** 2  # using an operator
print(new_df)
new_df['Value'] = numpy.sqrt(new_df['Value']) # using a numpy function.  You can't use math.sqrt() on a Series.
print(new_df)
new_df['EvenOdd'] = new_df['Value'].map(lambda x : 'Even' if x % 2 == 0 else 'Odd') # the map method for a Series
print(new_df)
new_df['Value'] = new_df['Value'].astype(int) # type conversion method for a Series
print(new_df)
```
The map() method takes one parameter, a function that does the conversion.  In the example above, a lambda is used to specify the function, and a ternary expression is used in the lambda.

## **Utility Methods**

### **Changing Column Names**

You can rename one or more columns as follows:

```python
joined_df.rename(columns={'Score':'Test Score'}, inplace=True)
print(joined_df)
```

### **Converting a Column To An Index**

```python
renamed_df=joined_df.set_index('Name')
print(renamed_df)
```

### **Sorting a DataFrame**

You can sort a DataFrame by column values: 

```python
joined_df.sort_values(by='Score',ascending=False,inplace=True)
print(joined_df)
```

### **Resetting the Index***

After you sort, the index values are no longer in order.  In this and other cases, you may want to reset the index:

```python
joined_df.reset_index(inplace=True, drop=True)
print(joined_df)
```

---

## **Check for Understanding**

1. **How can you select rows where the "Age" column is greater than 25?**
   - A) `df.loc[df['Age'] > 25]`
   - B) `df.iloc[df['Age'] > 25]`
   - C) `df[['Age'] > 25]`
   - D) `df[df['Age'] > 25]`

2. **Which method is used to combine two DataFrames on their indices?**
   - A) `join()`
   - B) `merge()`
   - C) `groupby()`
   - D) `concat()`


<details>

<summary>Answer</summary>

**Answer Key:**
1. A or D  
2. A  

</details>
---

## **Summary**

In this lesson, you’ve learned:
- How to select and slice subsets of data using `.loc[]` and `.iloc[]`.
- How to use `groupby()` for aggregations like `sum()` and `mean()`.
- How to combine DataFrames using `merge()` and `join()`.
- How to transform the data.
- Some utilities to rename columns, sort, convert a column to an index, and reset the index.

Use these techniques to perform advanced data analysis in Pandas. For further exploration, refer to the [Pandas Documentation](https://pandas.pydata.org/docs/) and Python's [official documentation](https://docs.python.org/3/).
```
