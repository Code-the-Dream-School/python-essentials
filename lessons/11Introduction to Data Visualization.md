
# **Lesson 11 — Introduction to Data Visualization**

## **Lesson Overview**
**Learning objective:** In this lesson, students will learn to create and customize both basic and advanced data visualizations using Python libraries such as Matplotlib and Seaborn. By the end of this lesson, students will be able to effectively tell stories with data using visual representation, enhancing their ability to communicate insights.

### **Topics:**
1. Introduction to Matplotlib: Creating basic plots (line, bar, histogram).
2. Customizing Plots: Labels, titles, legends, and colors.
3. Introduction to Seaborn: Creating advanced visualizations (heatmaps, pair plots).
4. Advanced Customization: Subplots, color palettes, and annotations.

---

## **11.1 Introduction to Matplotlib**

### **Setup**

You should run each of the code examples below from within your `python_homework` directory.  You need several additional libraries, so within `python_homework`, do the following:

```bash
pip install matplotlib
pip install seaborn
```

### **Overview**
Matplotlib is a foundational Python library for creating static, animated, and interactive visualizations. It is highly customizable and widely used for a variety of chart types, from basic plots to more complex visualizations.

### **Key Plot Types:**
1. **Line Plot:** Shows trends over time or continuous data.
2. **Bar Plot:** Compares categorical data.
3. **Histogram:** Displays the distribution of numerical data.

### **When to Use:**
- **Line Plot**: Best used when you want to display **trends over time** or track changes in continuous data, such as revenue, stock prices, or temperature variations.
- **Bar Plot**: Ideal for comparing **categorical data**, such as sales by region, number of items sold by category, or performance scores across different teams.
- **Histogram**: Used to display the **distribution** of a continuous variable and to detect outliers, skewness, or the normality of data.

### **Example Code: Creating Basic Plots**

These examples should be run from the Python interactive shell.  Each `show()` operation causes a graphics window to open, and the processing in the shell (or in a Python program running within your terminal) stops until you close that window.  The graphics window has several controls.  One brings up some sliders, allowing you to change the appearance of the chart or plot.  Another button allows you to save the image.  Using these buttons, you can create an image file that might be added to a document or slide or web page.  Experiment with these.  However, don't save the images within the `python_homework` folder, or they'll be delivered to your GitHub repository, and that wouldn't be useful.  For the assignment, you'll display plots using a Kaggle notebook.  When you do that, you don't see these buttons or sliders, and the graphics appear in the notebook itself, not in a separate window.  

Here are the examples you should try.  

```python
import matplotlib.pyplot as plt
import numpy as np

# Line Plot
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]
plt.plot(months, revenue, marker='o', linestyle='-', color='blue')
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.show()

# Bar Plot
categories = ["Region A", "Region B"]
sales = [500, 700]
plt.bar(categories, sales, color=['green', 'orange'])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.show()

# Histogram
random_data = np.random.randn(1000)
plt.hist(random_data, bins=30, color='purple', alpha=0.7)
plt.title("Random Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

### **Outcome:** 
- The **Line Plot** illustrates trends over time.
- The **Bar Plot** compares categorical data.
- The **Histogram** shows the distribution of random data.

The third example uses an interesting function, `randn()`.  This gives a random collection of values, but the random values cluster around the average value.  This is called a normal or Gaussian distribution, and many things in nature, such as people's heights, lifetimes of lightbulbs, sizes of snowflakes, and measurement errors in typical experiments, are roughly Gaussian.
---

## **11.2 Customizing Plots**

### **Overview**
Customizations make plots more informative and visually appealing. This includes:
- Changing colors, line styles, or bar widths.
- Adding grids to make value estimation easier.
- Using legends, titles, and labels for better context.

### **When to Customize:**
- **Line Plot Customization:** Adjust the style (dashed, dotted, solid) and color of the line to match the importance or theme of the data. Adding markers can help highlight key points.
- **Bar Plot Customization:** Customize the width, color, and edge of bars for visual distinction between categories.
- **Histogram Customization:** Customize bin sizes, color, and alpha (transparency) to enhance the data’s visibility and readability.

Run these examples in the Python shell.  
### **Example Code: Customizing Plots**
```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]

# Customized Line Plot
plt.plot(months, revenue, marker='o', linestyle='--', color='red', linewidth=2)
plt.title("Monthly Revenue", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(["Revenue"], loc="upper left")
plt.show()

# Customized Bar Plot
plt.bar(categories, sales, color=['skyblue', 'salmon'], width=0.5, edgecolor='black')
plt.title("Sales by Region", fontsize=14, fontweight='bold')
plt.xlabel("Region", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)
plt.show()
```

### **Key Customization Features:**
- Line Plot customization includes adjusting line style, color, and adding a grid.
- Bar Plot customization changes the bar color, width, and adds gridlines for better readability.

---

## **11.3 Introduction to Seaborn**

### **Overview**
Seaborn is a powerful Python visualization library built on top of Matplotlib. It simplifies the creation of complex statistical plots and integrates well with Pandas DataFrames. Seaborn provides better default aesthetics for some plots, making them visually appealing with minimal effort.

### **Key Plot Types:**
1. **Heatmap:** Visualizes correlation or relationships in tabular data.
    As was discussed in an earlier lesson, there might be a correlation between variables in a dataset.  Correlations are typically expressed as a number between -1.0 and 1.0.  A strong positive correlation is a positive number that is above, say, 0.3.  For people, there is a positive correlation between height and weight, for example.  A strong negative correlation is a negative number that is less than, say, -0.3.  For gas powered cars, there is a negative correlation between engine displacement and miles per gallon.  Even small correlations may be statistically meaningful if you have enough accurate measurements.  The heat map presents the correlations as a grid, where the positive correlations might be redder and the negative correlations might be bluer.

2. **Pair Plot:** Displays pairwise relationships between multiple variables.
    One form of the pair plot is the scatter plot.  Each dot on the plot represents one observation.  If there is a good correlation between the paired values, the points may line up.  You can also give a color for each dot, depending on the value of yet another column.  In the case of vehicles, you might have vehicle weight plotted vs. miles per gallon, and then you might have the dots colored by horsepower.  For a given horsepower, the mpg vs. vehicle weight might line up, but then you'd have high horsepower cars that are off of this line in one direction, indicated by a particular color.  One can customise the plot in various ways, such as by showing countour lines instead of individual dots.

### **When to Use:**
- **Heatmap**: Ideal for visualizing **correlations** or **relationships** in matrix-style data, such as the correlation between different features in a dataset.
- **Pair Plot**: Great for **multivariate analysis**, where you want to explore relationships between multiple features in a dataset.

For the example below, you use the Titanic dataset.  This dataset is built into Seaborn, so you can do sns.load_dataset().  In more typical cases, you load CSV files using pandas.  The Titanic dataset has the following columns:

- survived: True or False.
- pclass: Passenger class, meaning what kind of ticket or accomodation the passenger had.
- age
- sibsp: How many siblings or spouses each passenger had on the ship.
- parch: How many parents or children each passenger had on the ship.
- fare: How much the passenger's ticket cost.
- adult_male: True or False.
- alone: True or False, whether the passenger was traveling alone.

### **Example Code: Creating Advanced Visualizations**
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset: This dataset is 
titanic = sns.load_dataset("titanic")

# Heat map of correlations
plt.figure(figsize=(10, 6))
correlation_matrix = titanic.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(titanic, vars=["age", "fare", "adult_male"], hue="survived", palette="Set2")
plt.title("Pair Plot of Age, Fare, and Survival")
plt.show()
```

### **Outcome:**
- The **Heat Map** visualizes the correlation matrix of the Titanic dataset.
    Take a look at the heatmap, and assess which factors most important in affecting who survived.  Two factors made survival much less likely: Can you guess why?  One factor made survival more likely: Which one?

- The **Pair Plot** provides pairwise relationships between 'age', 'fare', and 'adult_male', as colored by whether these passengers survived.
    Some of these plots are not very useful.  Scatter plots where the variable on one of the axes only has two values are typically not very helpful, as you see.  The plots on the diagonal have a single variable plotted against itself, which doesn't seem too useful either, except that the default plot in this case is a "kde" plot, which shows the distribution of that single variable, as colored by who survived, and those plots do convey a story.

---

## **11.4 Advanced Customization**

### **Overview**
Advanced customization techniques include working with multiple subplots, adjusting figure sizes, and using color palettes to enhance the aesthetics of visualizations.

### **Key Concepts:**
- **Subplots:** Create multiple plots in one figure.
- **Color Palettes:** Use predefined or custom color palettes for better aesthetics.
- **Annotations:** Add text annotations to specific points on the plot.

### **When to Customize Further:**
- **Subplots**: Useful for comparing multiple visualizations in one figure, especially when you want to show different types of plots.
- **Color Palettes**: Enhance visual appeal and help in distinguishing between categories.
- **Annotations**: Add extra context or insights to specific parts of a plot.

### **Example Code: Advanced Customization**
```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

categories = ["Region A", "Region B"]
sales = [500, 700]
random_data = np.random.randn(1000)

# Subplot Example
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Left plot: Bar Plot
axes[0].bar(categories, sales, color=['skyblue', 'salmon'])
axes[0].set_title("Sales by Region")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Sales ($)")

# Right plot: Histogram
axes[1].hist(random_data, bins=30, color='purple')
axes[1].set_title("Random Data Distribution")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# Using a Custom Color Palette in Seaborn
sns.set_palette("muted")
sns.barplot(x=categories, y=sales)
plt.title("Sales by Region with Custom Palette")
plt.show()
```

### **Key Techniques:**
- **Subplots** allow the creation of multiple plots in a single figure for better comparison.
- Seaborn’s **custom color palette** gives more control over the visual appearance.

---

## **Summary**

In this lesson, you learned:
1. How to create basic visualizations (line plots, bar plots, histograms) using Matplotlib.
2. Techniques for customizing plots to improve readability and presentation.
3. How to use Seaborn for advanced statistical visualizations like heatmaps and pair plots.
4. Advanced techniques for creating subplots, using color palettes, and adding annotations for more insightful visualizations.

For more details, explore the [Matplotlib Documentation](https://matplotlib.org/stable/contents.html), [Seaborn Documentation](https://seaborn.pydata.org/), and the [Python Data Visualization](https://matplotlib.org/stable/gallery/index.html).

---

### Additional Resources:
1. **Matplotlib Tutorials:** For more detailed Matplotlib tutorials, check out [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html).
2. **Seaborn Gallery:** Explore different plot examples at the [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html).
3. **Data Visualization in Python:** To explore more about data visualization strategies and best practices, visit [Data Visualization in Python](https://realpython.com/python-data-visualization-using-matplotlib/).

