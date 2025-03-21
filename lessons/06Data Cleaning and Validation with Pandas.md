
# **Lesson 06 — Data Cleaning and Validation with Pandas**

## **Lesson Overview**
**Learning objective:** Students will learn to apply fundamental data cleaning and validation techniques using Pandas. These include handling missing data, transforming data types, removing duplicates, managing outliers, standardizing text data, and validating data ranges.

### **Topics:**
1. Handling Missing Data
2. Data Transformation
3. Using Regular Expressions
4. Removing Duplicates
5. Handling Outliers
6. Standardizing Data
7. Validating Data Ranges
8. Handling Categorical Data
9. Handling Inconsistent Data
10. Feature Engineering

---

## **6.1 Handling Missing Data**

### **Overview**
Missing data can affect the accuracy and reliability of analysis. Common approaches include removing or replacing missing values.

### **Key Methods:**
- `dropna()`: Removes rows or columns with missing values.
- `fillna()`: Replaces missing values with specified replacements like the mean, median, or a default value.

### **Why Handle Missing Data?**
- Ensures consistent dataset formatting.
- Avoids errors during calculations.
- Preserves data integrity.

### **Code Example:**
```python
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', None, 'Charlie', 'David'],
        'Age': [24, None, 22, 35],
        'Salary': [50000, 60000, None, None]}
df = pd.DataFrame(data)

# Drop rows with missing data
df_dropped = df.dropna()

# Replace missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'Salary': 0})

print("DataFrame with missing data handled:")
print(df_filled)
```

### **Explanation:**
- `dropna()` removes any row that contains a `None` (missing) value.
- `fillna()` is used to replace missing values. In this case, the `Age` column's missing values are replaced with the mean, and the `Salary` column's missing values are filled with 0.

---

## **6.2 Data Transformation**

### **Overview**
Data transformation converts data into consistent formats and types for easier analysis and calculations.

### **Key Tasks:**
- Converting data types.
- Formatting date columns for temporal analysis.

### **Why Transform Data?**
- Ensures compatibility with numerical and time-based functions.
- Reduces inconsistencies in datasets.

### **Code Example:**
```python
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'Join_Date': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Age' to integer
df['Age'] = df['Age'].astype(int)

# Convert 'Join_Date' to datetime
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

print("Transformed DataFrame:")
print(df)
```

### **Explanation:**
- `astype(int)` converts the `Age` column, originally stored as strings, into integers.
- `pd.to_datetime()` converts the `Join_Date` column into Python’s datetime objects for easier date manipulation and comparison.

---

## **6.3 Using Regular Expressions

### To be added

## **6.4 Removing Duplicates**

### **Overview**
Duplicates can distort analysis by inflating metrics or introducing bias. Identifying and removing them ensures data quality.

### **Key Method:**
- `duplicated()`: Identifies duplicates.
- `drop_duplicates()`: Removes duplicate rows.

### **Code Example:**
```python
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 35],
        'Salary': [50000, 60000, 50000, 80000]}
df = pd.DataFrame(data)

# Remove duplicates
df_no_duplicates = df.drop_duplicates()

print("DataFrame with duplicates removed:")
print(df_no_duplicates)
```

### **Explanation:**
- `drop_duplicates()` removes rows where the entire record is a duplicate of another.
- `drop_duplicates(subset='Name')` removes rows where the `Name` column is duplicated, keeping only the first occurrence of each name.

---

## **6.5 Handling Outliers**

### **Overview**
Outliers are extreme values that deviate significantly from other observations and can bias statistical calculations.

### **Common Approach:**
- Replace outliers with statistical measures like the median.

### **Code Example:**
```python
# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

print("DataFrame after handling outliers:")
print(df)
```

### **Explanation:**
- Outliers in the `Age` column that are greater than 100 or less than 0 are replaced by the median value of the `Age` column.

---

## **6.6 Standardizing Data**

### **Overview**
Standardizing text data ensures consistency, making it easier to group, filter, and analyze.

### **Key Techniques:**
- Convert text to lowercase and strip whitespace.
- Standardize inconsistent entries.

### **Code Example:**
```python
# Standardize 'Name' column
df['Name'] = df['Name'].str.lower().str.strip()

# Standardize 'City' column with mapping
df['City'] = df['City'].replace({'ny': 'New York', 'la': 'Los Angeles'})

print("Standardized DataFrame:")
print(df)
```

### **Explanation:**
- The `Name` column is standardized by converting all entries to lowercase and stripping any extra whitespace.
- The `City` column is standardized by replacing `ny` with `New York` and `la` with `Los Angeles`.

---

## **6.7 Validating Data Ranges**

### **Overview**
Validating data ranges ensures all values fall within acceptable limits, avoiding invalid or erroneous data.

### **Example Task:**
- Ensure ages are between 18 and 65. Replace invalid values with `NaN` and fill them with the median.

### **Code Example:**
```python
# Replace invalid ages with NaN
df['Age'] = df['Age'].apply(lambda x: x if 18 <= x <= 65 else None)

# Fill missing values with median
df['Age'] = df['Age'].fillna(df['Age'].median())

print("DataFrame after validating age ranges:")
print(df)
```

### **Explanation:**
- Any age outside the range of 18 to 65 is replaced with `None` (NaN).
- Missing values in the `Age` column are filled with the median value of the column.

---

## **6.8 Handling Categorical Data**

### **Overview**
Handling categorical data involves encoding non-numeric values, which is especially useful for machine learning models that require numerical input.

### **Key Techniques:**
- **Label Encoding**: Converting each category into a number.
- **One-Hot Encoding**: Creating binary columns for each category.

### **Why Handle Categorical Data?**
- Many machine learning algorithms require numerical data.
- Proper encoding helps preserve the relationships between categories.

### **Code Example:**
```python
# Sample DataFrame with categorical data
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# Label encoding: Convert categories to numbers
df['Color_Label'] = df['Color'].map({'Red': 1, 'Blue': 2, 'Green': 3})

# One-Hot Encoding: Create binary columns for each category
df_encoded = pd.get_dummies(df['Color'], prefix='Color')

print("DataFrame with Categorical Data Handled:")
print(df_encoded)
```

### **Explanation:**
- **Label Encoding** maps the `Color` column's categories to integer values.
- **One-Hot Encoding** creates binary columns for each unique value in the `Color` column.

---

## **6.9 Handling Inconsistent Data**

### **Overview**
Inconsistent data can result from typos, different formats, or various naming conventions. Handling inconsistencies ensures uniformity in the dataset.

### **Key Techniques:**
- **Fuzzy Matching**: Identifying and standardizing similar but non-exact values.
- **Regex (Regular Expressions)**: Using patterns to extract or replace inconsistent data.

### **Why Handle Inconsistent Data?**
- Improves the quality of data for analysis.
- Helps identify patterns across otherwise unmatchable data points.

### **Code Example:**
```python
import re

# Sample DataFrame with inconsistent data
data = {'City': ['New York', 'new york', 'San Francisco', 'San fran']}
df = pd.DataFrame(data)

# Standardize text data (convert to lowercase and strip spaces)
df['City'] = df['City'].str.lower().str.strip()

# Use Regex to replace shorthand names
df['City'] = df['City'].replace({'san fran': 'san francisco'})

print("DataFrame with Inconsistent Data Handled:")
print(df)
```

### **Explanation:**
- **String standardization**: Converts all entries in the `City` column to lowercase and removes extra spaces.
- **Regex**: Matches and replaces shorthand for cities with their full names.

---

## **6.10 Feature Engineering**

### **Overview**
Feature engineering involves creating new features from existing ones to enhance the dataset and provide more insights.

### **Key Techniques:**
- **Binning**: Categorizing continuous data into discrete bins.
- **Polynomial Features**: Generating interaction terms or polynomial features for regression models.

### **Why Feature Engineering?**
- New features can reveal hidden patterns and relationships.
- Improves model performance in machine learning.

### **Code Example:**
```python
# Sample DataFrame with numerical data
data = {'Age': [24, 35, 30, 45, 60]}
df = pd.DataFrame(data)

# Binning Age into age groups
bins = [0, 30, 60, 100]
labels = ['Young', 'Middle-Aged', 'Old']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print("DataFrame after Feature Engineering:")
print(df)
```

### **Explanation:**
- **Binning**: Converts `Age` into categories like 'Young', 'Middle-Aged', and 'Old' based on defined intervals.

---

## **Summary**

In this lesson, you learned how to:
1. Handle missing data with `dropna()` and `fillna()`.
2. Transform data types and formats.
3. Remove duplicate records.
4. Identify and manage outliers.
5. Standardize text data for consistency.
6. Validate data ranges to ensure accuracy.
7. Handle categorical data with encoding methods.
8. Address inconsistent data with fuzzy matching and regex.
9. Apply feature engineering for better insights and analysis.

These techniques are essential for maintaining clean, reliable datasets, ready for analysis. Explore the [Pandas Documentation](https://pandas.pydata.org/docs/) to deepen your understanding.
