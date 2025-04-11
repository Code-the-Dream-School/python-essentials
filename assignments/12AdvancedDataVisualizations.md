

This assignment is to be created in the `assignment12` folder of your `python_homework` directory.  Be sure that you create an `assignment12` git branch for the files you create.

---


## **Task 1: Plotting with Pandas**
1. Create a file called employee_results.py.
2. Load a DataFrame called employee_results using SQL.  You connect to the `../db/lesson.db` database.  You use SQL to join the employees table with the orders table with the line_items table with the products table.  You then group by employee_id, and you SELECT the last_name and revenue, where revenue is the sum of price * quantity.  Ok, that's a lot of SQL to mess with, so here is the statement you need:
   ```SQL
   SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN Orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;
   ```
3. Use the Pandas plotting functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue.
4. Give appropriate titles, labels, and colors.
5. Show the plot.

## **Task 2: A Line Plot with Pandas**
1. Create a file called cumulative.py.  The boss wants to see how money is rolling in.  You use SQL to access `../db/lesson.db` again.  You create a DataFrame with the order_id and the total_price for each order.  This requires joining several tables, GROUP BY, SUM, etc.
2. Add a "cumulative" column to the DataFrame.  This is an interesting use of apply():
   ```python
   def cumulative(row):
      totals_above = df['total_price'][0:row.name+1]
      return totals_above.sum()

   df['cumulative'] = df.apply(cumulative, axis=1)
   ```
   Because axis=1, apply calls the cumulative function once per row.  Do you see why this gives cumulative revenue?
3. Use Pandas plotting to create a line plot of cumulative revenue vs. order_id.
4. Show the Plot.

## **Task 3: Interactive Visualizations with Plotly**
1. Load the Plotly wind dataset, via the following:
   ```python
   import plotly.express as px
   import plotly.data as pldata
   df = pldata.wind(return_type='pandas')
   ```
   Print the first and last 10 lines of the DataFrame.
2. Clean the data.  You need to convert the 'strength' column to a float.  Use of str.replace() with regex is one way to do this, followed by type conversion.
3. Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
4. Save and load the HTML file, as `wind.html`.  Verify that the plot works correctly.

## **Task 4: A Dashboard with Dash**

Ok, deep breath.  Start by copying `lesson12_c.py` to `gdp_growth.py`. We can reuse the template.

1. The dataset to use is the Plotly built in `gapminder` dataset.  This has, among other things, the per capita GDP for various countries for each year.  For a given country, there will be one row per year.  This means that the 'countries' column has many duplicates.
2. You want a dropdown that has each unique country name. You create a Series called `countries` that is the list of countries with duplicates removed.  You use this Series to populate the dropdown.  Give the dropdown the initial value of 'Canada'.
3. You give the dropdown the id of 'country-dropdown' and also create a dcc.Graph with id 'gdp-growth'.
4. You create the decorator for the callback, associating the input with the dropdown and the output with the graph.
5. The decorator decorates an `update_graph()` function.  This is passed the country name as a parameter.  You need to filter the dataset to get only the rows where the country column matches this name.  Then you create a line plot for 'year' vs. 'gdpPercap`.  Give the plot a descriptive name that includes the country name.
6. The line to run the app doesn't need to change.
7. Run the program, and check it out in the browser.  Make bug fixes as needed.

---

## **Task 4: Reflection**
1. Reflect on the differences between static and interactive visualizations.
2. Write a short paragraph discussing the advantages of using dashboards for real-time data exploration.
3. Explain how interactive tools like Plotly and Dash can improve data communication in professional settings.

---

## **Task 5: Extension Task(Optional)**
1. Extend the dashboard to include:
   - A date range selector for filtering data.
   - Multiple charts displayed simultaneously (e.g., line and bar charts side by side).
2. Document your extended dashboard setup and discuss its applications in business or research.

### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment12` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment12` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**. 

---
