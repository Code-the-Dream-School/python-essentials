# Advanced Data Cleaning and Validation Assignment

### Data Cleaning and Validation with Pandas

### **Objective:**

This assignment is an approximation of a real world data cleaning case.  You have four copies of a dataset, each with errors.  You want to create a single authoritative dataset that cleans all the errors out.  In addition, you'll get practice in using regular expressions for data transformation.

This assignment is to be created in a Kaggle notebook, as you did for Assignments 4 and 5.  This time, create a notebook called CTD_Assignment_6 for code as described below.  As for all assignments that use notebooks, you should create a markdown cell above your code that marks the location where you completed each coding task.

Complete the tasks below to demonstrate your understanding of data cleaning and validation techniques. Submit your code and outputs for each task.

---
This assignment asks you to do some fairly serious data cleaning.  You will start from 4 CSV files.  Each of the files describes 400 people, with a name, address, zip, and phone number for each.  However:
1. Some of the people have the same name.

2. There are only 200 different addresses.  Some people share a house.

3. Of the people that share addresses, 20% also share a phone number.

4. Each of the CSV files record this information, **but there are errors in each of the files.** The errors are different in each of the files.

5. In 15% of the records, the phone number is missing.

6. In another 15% of the records, the phone number is incorrect.

7. In 20% of the records, the zipcode is missing.

8. In 15% of the records, the name is misspelled.

9. In 15% of the records, the address is misspelled.

10. Some rows may have more than one error.

Your task is to create a dataset with 400 rows, one for each of the people, that corrects these errors by comparing the versions in each of the files.

## Task 1: How Would You Solve This?

1. Think: How would you do this, using the power of Pandas?

2. Create a markdown cell in your notebook.  Write down a list of 5 or so ideas about how you could do this.  You do not need to use markdown -- plain text will suffice.


## Task 2: Load Dataset ##

1. In your notebook, click on the "Add Input" button in the upper left, and then on "Datasets".  Do a search on "Code The Dream Assignment 6", and then on the plus sign next to that dataset to add it to your notebook.  Run the first cell of the notebook to resolve the file names.

2. Create a code cell.  Within it, import pandas and load the four CSV files into four DataFrames.  Print out the first 5 lines of one of these DataFrames, so that you understand the data shape.  Each of the datasets is similar.

3. You need an additional package, called "thefuzz".  This package does approximate matching of text strings.  However, it is not part of the standard library delivered with Kaggle, so you need to add this code:

```python
try: 
    from thefuzz import process 
except ImportError: 
    !pip install thefuzz 
    from thefuzz import process
```
4. Concatenate all 4 DataFrames into one, call it `df`.  Print out the info for df.  You should have 1600 rows, but there are NaN values and other problems.

## Task 3: Clean Up Spelling Errors

We know that some of the names are misspelled.  We are going to assume that 3 of the spellings are correct, and that the remainder is bad.  Of course, several people have the same name, and some people have the same address, so that for a given name, or a given address, there may be more than 4 rows.  But, we'll assume that if a name or address is spelled the same way 3 or more times, that's the correct spelling.

1. Find the list of correct names.  You use the value_counts() method, which returns a Series.  In the Series, the index is the list of names, and the values are the count for each.  As follows:
   ```python
   df_names = df.value_counts('Name')
   names = list(df_names[df_names > 2].index)
   ```
   Print out the first 10 entries of the list of names.

2. Ok, now we have the list of good names.  What do we do about the bad ones?  We want to replace each with the good name that is most similar to it, using the `thefuzz` package. As follows:
   ```python
   df['Name'] = df['Name'].map(lambda x : x if x in names else process.extractOne(x, names)[0])
   ```
   Here, process.extractOne() goes through the list of good names to find the best match.  It returns a tuple, where the first element is the match, and the second is a number that indicates how good the match is.

3. Fix the addresses the same way.

## Task 4: Clean Up the Zip and Phone Columns

We now have four versions of the information for each person.  We can compare these and, one would hope, we can find the right values, basically by collecting the votes from each.  This is a new technique, so the answer is as follows:

```python
def fix_anomaly(group): 
    group_na = group.dropna() 
    if group_na.empty: 
        return group.values 
    mode = group_na.mode() 
    if mode.empty: 
        return group.values 
    return mode.iloc[0]

df['Zip'] = df.groupby(['Name', 'Address'], as_index=False)['Zip'].transform(fix_anomaly).reset_index(drop=True)
```
Let's explain this code.  
- We do a groupby() for name and address.  The records where the both the name and address are the same are for the same person.  
- We use as_index=False because we don't want to change the indexing.  
- Then we do a transform() on the Zip column.  This works kind of like the map() function, but you are passed each group in turn.  
- Each time we get a group of values, we collect the votes.  First we do a dropna(), because a NaN value doesn't get a vote.  Then we use the mode() function to find the most common value, and change the value for the entire group to match.  
- There may be several modes, for example if there are 2 of one value and 2 of another, so we just take the first mode. (Actually this is a little dangerous, because one of the other modes might be the correct one.  The correct approach might be to leave the values unchanged if there is more than one mode.)  
- We have to handle a couple of edge cases.  First, all the values may be NaN, in which case we have nothing to do.  Second, there may be no mode.  This happens if each of the non-null values occurs once.  So then we just leave the values unchanged, because we don't know which one to use. After the transform() completes, we are done with the groupby(), so we reset the index.

1. Fix the phone number column the same way.  Hint: You can reuse fix_anomaly().

## Task 5: The Final Consolidation

1. Eliminate duplicate records.

2. Print out the first 10 records of the resulting DataFrame.

3. Print out the info for the end DataFrame.

Hmm.  413 records reported by info().  We were hoping for 400 authoritative records.  And, we still have some records with null values.  So, next step:

## Task 6: Failure Analysis

Validation of the final result, and failure analysis for whatever isn't working right, is a critical part of data cleaning.

1. Print out all the rows that have null values.  (Note: This only finds some of the errors, as there are still erroneous records that have no null values.)

2. We can now subset the original data to figure out what went wrong.  So, add a line to save a copy of the df dataframe, as it was right after the concatenation.  Call the copy df_save.

3. In the records that have null values, you see one for "Tammie ThoXXmas".  This looks like a misspelling that should have been corrected.  Print out all the rows from df_save that have the name "Tammie ThoXXmas".  Can you see what is wrong?

4. Here's the answer: There are two people named Tammie Thomas, one in Minnesota, one in Massachusetts.  So the original dataset had 8 entries for the two people with that name.  And, in three of them, the name is misspelled in exactly the same way.  Can you see why this would cause trouble for our code?  This is exactly the sort of thing that happens with real-world data.

5. We see that there is also a problem for "Charles Smith".  Print out all the rows from df_save that have this name.

## Task 7: How to Improve

1. Create another markdown cell.  Explain what happened for "Tammie ThoXXmas", so that this name was not corrected.

2. Also, in the markdown cell, explain why the approach failed for "Charles Smith".

3. What could be done to make the data valid?  Put your ideas into the markdown cell.  Hint: The solution is often not more code.

## Task 8: Regular Expressions for Data Cleaning

**To Be Added**

---

### **Submit the Notebook for Your Assignment**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy the public URL to your clipboard.

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
