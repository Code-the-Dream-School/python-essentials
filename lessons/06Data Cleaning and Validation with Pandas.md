
# **Lesson 06 — Data Cleaning and Validation with Pandas**

## **Lesson Overview**
**Learning objective:** Students will learn to clean and standardize real-world datasets using Pandas. They will handle missing data, outliers, duplicates, inconsistent formatting, and categorical variables, while also applying transformations and basic feature engineering techniques to prepare data for analysis or modeling.


### **Topics:**
1. **Handling Missing Data**: Using `dropna()` and `fillna()` to manage null values.
2. **Data Transformation**: Changing data types and formatting dates for analysis.
3. **Using Regular Expressions**: Using regex with `str.replace()`, `extract()`, and `contains()` in Pandas.
4. **Removing Duplicates**: Identifying and removing repeated rows with `drop_duplicates()`.
5. **Handling Outliers**: Replacing extreme values with statistical measures like the median.
6. **Standardizing Data**: Lowercasing, trimming whitespace, and mapping values for consistency.
7. **Validating Data Ranges**: Ensuring numeric values fall within expected bounds.
8. **Handling Categorical Data**: Encoding categories with label encoding and one-hot encoding using `get_dummies()`.
9. **Handling Inconsistent Data**: Using regex and string methods to normalize inconsistent entries.
10. **Feature Engineering**: Binning continuous variables into categories with `pd.cut()`.

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

## **6.3 Using Regular Expressions**

### A brief introduction to regular expressions

#### History
- Invented as a theoretical framework in 1951 by Stephen Cole Kleene
- First used in 1968 for the QED text editor (Ken Thompson)
- Used in a variety of Unix tools in the 1970's (ed, lex, vi, grep, awk, emacs)
- Now the most popular string pattern matching language, available in almost all programming languages
- Most standardized on the perl version which is more powerful and less verbose than other standards

#### Regular expression syntax and matching
- Python provide regular expressions through the standard library [re module](https://docs.python.org/3/library/re.html)
- The [regex HOWTO](https://docs.python.org/3/howto/regex.html#regex-howto) provides a tutorial on usage
- For more practice with regexes [regex101](https://regex101.com/) is a useful site.
- Raw strings (`r''`) are preferred for regexes in python to avoid excessive `'\'` characters
- All regular characters match themselves
- Meta characters extend patterns for more complex matches
  - Meta-characters can be included in patterns by escaping with `‘\’`
  - `<pattern>*` : match 0 or more copies of pattern
  - `<pattern>+` : match 1 or more copies of pattern
  - `<pattern>{n}` : match exactly `n` copies of the pattern
  - `<pattern>?` : match 0 or 1 times
  - `^<pattern>` : match only at the beginning
  - `<pattern>$` : match only at the end
  - Character sets: `[a-z0-9]` – match any of the characters in the set
  - Excluding characters: `[^A-Z]` `^` means match characters not in the set (e.g. anything but capital letters)
    - `^` has a different meaning in this context, specifying a character exclusion rather than the start of the string
  - `\d` : match digits (short for `[0-9]`), `\D` not a digit
  - `\w` : match any alphanumeric (word - short for `[a-zA-Z0-9_]`), `\W` not a word character
  - `\s` : match whitespace, `\S` not a whitespace character
  - `.` : match any character except newline. Use `\.` to match a period.  I general `\` escapes special characters.
  - Use `|` to specify alternates: `[0-9]+|[a-z]+`:  e.g. match digits or lowercase letters
    - Surrounding the alternative by `()` limits the scope of the alternatives e.g. `r'start ([0-9]+|[a-z]+) end'`.  This also introduces a match group which is not necessarily used.
  - Group using `()` to capture substrings

#### Examples
- `^[a-zA-Z]\w+`   # Must start at the beginning of the string with a letter followed by any word character
- `[0-9]+|[a-z]+`  # Match either one or more digits or one or more lowercase letters (but not both)
- `[a-z]|[0-9]+`   # Match one lowercase letter or one or more digits (but not both)
- `^\s*(\w+)\s*$`  # Capture a word which may have whitespace before or after

#### Debugging regular expressions

Regular expressions are greedy
- Eeach part of the pattern matches as many characters as possible
- Bugs often involve a part of the pattern matching too much (or all) of the rest of the string
- e.g. putting ^.+ at the beginning of the pattern will match all the characters
  - Leaving nothing for the rest of the pattern


### Using regular expressions with the Python Standard Library

In the python standard library [re module](https://docs.python.org/3/library/re.html), regular expressions are precompiled into a [pattern object](https://docs.python.org/3/library/re.html#re-objects).  The pattern object can then be matched against entire strings using the [match() method](https://docs.python.org/3/library/re.html#re.Pattern.match) or the [search() method](https://docs.python.org/3/library/re.html#re.Pattern.search) can be used to scan for the pattern in a string.  These methods return `None` if there is no match.  If there is a successful match, a [match object](https://docs.python.org/3/library/re.html#re.Match) is returned.  The [group() method](https://docs.python.org/3/library/re.html#re.Match.group) can be used to retrieve the entire match or subgroups defined using parentheses.  For this class, we will be using regular expressions with Pandas as describe below, however it can be helpful to use the standard library regular expressions to develop and test a pattern.  It's also an important part of the Python ecosystem.  Here are some examples:

```python
import re
# compile the regular expression
# This regex captures the username from a gmail address as a subgroup
# It requires one or more word chacaters at the beginning, then any number of words, digits, periods and '-''s
# The first `()` will be available a group(1) if there is a match
gmail = re.compile(r'(\w+[\w\d\.\-]*)@gmail.com')
search_target = 'Boa-Dreamcode.public@gmail.com'
# match the entire string
match = gmail.match(search_target)
# print the group and subgroup
print(match.group()) # => Boa-Dreamcode.public@gmail.com (same as group(0))
print(match.group(1)) # => Boa-Dreamcode.public
# now serch within a longer string
search_target = 'My email is Boa-Dreamcode.public@gmail.com, what is yours?'
match = gmail.search(search_target)
print(match.group()) # => Boa-Dreamcode.public@gmail.com (same as group(0))
print(match.group(1)) # => Boa-Dreamcode.public
```

### Using regular expressions with Pandas
  
 Pandas [Series.str](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling) provides a variety of methods which access or manipulate the values of a Series as strings.  Many of these methods support regular expressions.  All of the examples below assume you have imported `pandas as pd`.  The [Series.filter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.filter.html#pandas.Series.filter) method also supports regular expressions.  The methods available with `Series.str` are different from those provided by the builtin `str` type.

 #### Using `replace`

 Sometimes phone numbers or ID fields can contain non-numeric characters (such as dashes, parentheses, or letters) that you want to remove.

 ```python
 df = pd.DataFrame({
    'phone_number': ['(123) 456-7890', '+1-555-123-4567', '555.456.7890']
})
# Remove all non-digit characters
df['phone_number_clean'] = df['phone_number'].str.replace(r'\D', '', regex=True)
print(df)
```

Removing html tags from scraped data.

```python
df = pd.DataFrame({
    'html_content': [
        '<p>This is a paragraph.</p>',
        '<div>Some <strong>bold</strong> text</div>'
    ]
})
# <.*?> matches <, then any characters as few as possible (.*? is a non-greedy match), then >
df['text_only'] = df['html_content'].str.replace(r'<.*?>', '', regex=True)
print(df)
```

#### Using `extract`

Capture the domain name from email addresses.  Note that the `extract` method only uses regular expressions, whereas they are optional and must be specified for `replace`.

```python
df = pd.DataFrame({
    'email': [
        'john.doe@example.com',
        'jane_smith@my-domain.org',
        'user123@anotherdomain.net'
    ]
})
df['domain'] = df['email'].str.extract(r'@(\w+[\w\.-]+)')
print(df)
```
Match groups can be given names.  When named groups are used with the `dataFrame.extract` method the group names are used as column names in the resulting `DataFrame`.

```python
series = pd.Series(['Tom-25-USA', 'Anna-30-UK', 'John-22-Canada'])
pattern = r'(?P<Name>\w+)-(?P<Age>\d+)-(?P<Country>\w+)'
result = series.str.extract(pattern)
print(result)

```

#### Using `contains`

Get all rows which contain valid emails.

```python
df = pd.DataFrame({
    'email': ['test@example.com', 'invalid-email', 'hello@mydomain.org']
})
valid_emails = df[df['email'].str.contains(r'^\w+[\w\.-]*@\w+[\w\.-]+\.\w+$')]
print(valid_emails)
```
#### Combining filters using bitwise operators
The `contains` method returns a `Series` of boolean values also known as a filter.  Bitwise operators (&, |, ~) can be used to combine or invert filters.  Don't confuse these with the boolean operators (`and`, `or`, and `not`). Also, note that the raw strings used to define regular expressions can be entered on multiple lines.  Regexs can be long, and listing them on multiple lines improves readability.  Here a series of alternatives are listed one per line with a trailing `'|'`.  Note that they aren't separated by commas.

```python
orders = [
    "Order 1: 2x Cheddar, 1x Gouda",
    "Order 2: 3x Stilton, 2x Rye Crackers",
    "Order 3: 2x Saltines",
    "Order 4: 1x Camembert, 2x Jahrlsberg",
    "Order 5: 2x Gouda, 2x Rye Crackers",
    "Order 6: 1x Ritz, 1x Jahrlsberg",
    "Order 7: 1x Parmesan, 1x Brie",
    "Order 8: 3x Saltine Crackers",
    "Order 9: 2x Rye Crackers",
    "Order 10: 2x Mozzarella, 1x Cheddar",
    "Order 11: 1X Water Crackers"
    "Order 12: 3x Blue Cheese",
    "Order 13: 1x Triscuits",
    "Order 14: 1x Butter Crackers, 2x Multigrain Crackers",
    "Order 15: 1x Feta",
    "Order 16: 1x Havarti",
    "Order 17: 2x Wheat Crackers",
    "Order 18: 1x Ricotta",
    "Order 19: 1x Garlic Herb Crackers"
]
orders = pd.Series(orders)
favored_cheeses = orders.str.contains(r'Cheddar|'
                                       r'Stilton|'
                                       r'Camembert|'
                                       r'Jahrlsberg|'
                                       r'Gouda', case=False, regex=True)
favored_crackers = orders.str.contains(r'Ritz|'
                                       r'Triscuit|'
                                       r'Rye Crackers|'
                                       r'Multigrain Crackers|'
                                       r'Water Crackers', case=False, regex=True)
print(orders[favored_cheeses | favored_crackers])
print(orders[favored_cheeses & favored_crackers])
print(orders[~favored_cheeses])
```

#### Using `filter`

Instead of specifying columns one by one, you can select or drop columns whose names match a pattern using DataFrame.filter.

```python
df = pd.DataFrame({
    'col_2021': [1, 2, 3],
    'col_2022': [4, 5, 6],
    'col_other': [7, 8, 9]
})
# Select columns that end with digits
df_year = df.filter(regex=r'\d+$')  
print(df_year)
```

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
- Many machine learning algorithms require numerical data, so we need some way to convert categories into numbers.
- Proper encoding helps preserve the categorical structure in the data. There are different ways to represent categorical data numerically: with [one hot encoding](https://www.datacamp.com/tutorial/one-hot-encoding-python-tutorial) each category is represented in a binary fashion as present or absent: this is a very popular technique in machine learning. 
- In pandas, one-hot-encoding is implemented with the `get_dummies()` function. 

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
- - **One-Hot Encoding** use the `get_dummies()` function to create binary columns for each unique value in the `Color` column. 
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
Feature engineering involves creating new features from existing ones in raw data. 
This is typically used as a first step before the data is fed to machine
learning algorithms. We will go over one way to extract features from data, *binning*
into discrete categories, but [feature engineering is a large subfield of its own](https://www.ibm.com/think/topics/feature-engineering).

### **Key Techniques:**
- **Binning**: Categorizing continuous data into discrete bins.
- **Principal component analysis (PCA)**: for automated extraction of important combinations of features from high dimensional datasets (this is a fairly advanced topic, but if you are interested in an intuitive overview of PCA see [this video](https://www.youtube.com/watch?v=ZgyY3JuGQY8)). 

### **Why Feature Engineering?**
- New features can reveal hidden patterns and relationships.
- Reduce noise in the raw data.
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
