
# **Lesson 11: Introduction to Data Visualization**

This assignment is to be implemented in a Kaggle notebook, using a Kaggle dataset.  As usual, mark the section of code that implements each task with a markdown cell.

---

## **Task 1: Data Understanding**

1. In Kaggle, go to the Datasets link on the left side of the page.
2. Search for "Diabetes Health Indicators Dataset".  You should find one from Alex Teboul.
3. In Data Explorer on the right, click on the one that starts with "diabetes_012".
4. We need to understand particular columns.  Click on the pulldown for the 22 columns. Click on "Select All" and then "Apply".  Then select "Column" from the menu.  This explains the meaning of all the columns.  Scroll down throuh the information about each column.  You see that "Diabetes_012" can have 3 numeric values.  You see that "Age" is broken down into 13 buckets.  You see that "GenHlth" has values from 1 to 5, 5 being worst!  You see that PhysHlth is the number of days in the past month where the person's physical health was not good.  Again, a high number is bad!  We can't understand the plots we make **unless we know what the data means.**

## **Task 2: Creating the Notebook and Loading Data**

1. Create a Kaggle Notebook called "CTD_Assignment_11".  Add the "Diabetes Health Indicators Dataset".  Run the first cell so that you get the filenames.
2. Load the one that has "diabetes_012" in the name into a `diabetes` DataFrame.
3. Print out the first 5 lines of the DataFrame.

## **Task 3: A Bar Plot For Age Distributions**

1. Use Matplotlib to create a histogram of age distributions in the `diabetes` DataFrame, where the X axis is "Age" and the Y axis is "Count". Give the plot a meaningful title, and give the axes meaningful labels.
2. Show the plot to see if it is as you expect.

## **Task 4: General Health over Time**

1. Create a `health_by_age` DataFrame, using groupby() on the `diabetes` DataFrame.  Group by age.  Aggregate the `GenHlth` column using `mean`.
2. Add a column called "Health" to the resulting DataFrame.  The value of this should be 5 minus the `GenHlth` column.  It is usually more meaningful to have high values mean good and low values mean bad.
3. Sort `health_by_age` by the index.  (You use the sort_index() method.)  The index for this DataFrame is "Age", because of the groupby().
4. Use Matplotlib to create a line plot where the X axis is "Age" (the index) and the Y axis is "Health".  Add a meaningful title and axes labels.
5. Show the plot. It's kind of a sad story.

## **Task 5: A Heat Map of All Columns**

1. Create a correlation matrix called `diabetes_corr` for all columns.
2. Use Seaborn to create a heat map from the correlation matrix.  Note: It appears that Seaborn uses some Python deprecated features, so you will see warning messages.  You can ignore these.
3. Show the heat map.

As you will notice, this heat map is hard to read.  You solve that problem in the next task by subsetting the correlation matrix.

## **Task 6: Subset Heat Maps**

Suppose you decide that the data you care about most is in the "Diabetes_012", "HeartDiseaseorAttack", and "GenHlth" columns.

1. Create a subset correlation matrix called `diabetes_corr_subset`, selecting these columns from `diabetes_corr`.
2. Sort this in descending order on the `Diabetes_012` column.
3. Create a heatmap for the first 10 rows and show it.  These are the factors most strongly correlated with diabetes.
4. Create a heatmap for the last 10 rows, with an appropriate title, and show it.  These are the factors that are negatively correlated (or weakly correlated) with diabetes.
5. Sort the matrix again on the "GenHlth" column in descending order, and again show heat maps for the first and last 10 rows.
6. Notice the factors that are most consequential for diabetes and health, according to this dataset.  Add a markdown cell that describes these.

## **Task 7: A Pair Plot: Body Mass Index vs. Age

1. Using the `diabetes` DataFrame, create a pair plot for "BMI" and "Age", with a `hue` of "Diabetes_012".  I find that `palette=['#FF5733', '#33FF57', '#3357FF']` gives a helpful display.
2. Give the pair plot a descriptive title and show it.
3. The plot is hard to read.  There are too many values for BMI.  Use `qcut()` to divide BMI into 10 quantiles, and add the resulting Series to the `d_h_i` DataFrame.  Then plot Age vs. BMI Quantiles, with the same hue as before.
4. Give this pair plot a descriptive title and show it.

### **Submit the Notebook for Your Assignment**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy the public URL to your clipboard.

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
