
# **Lesson 12 — Advanced Data Visualization Techniques**

## **Lesson Overview**
**Learning objective:** In this lesson, students will learn how to create advanced and interactive visualizations using Python libraries like Pandas, Plotly, and Dash. By the end of this lesson, students will understand how to visualize data directly from DataFrames, create interactive plots, and build simple dashboards for real-time data exploration.

### **Topics:**
1. Plotting with Pandas: Visualizing data directly from DataFrames.
2. Interactive Visualizations: Using Plotly for interactive plotting.
3. Dashboards: Creating dynamic dashboards with Plotly and Dash.
4. Advanced Customization: Advanced interactivity, subplots, and real-time updates.

### **Setup**

You need several new libraries for this lesson.  Within your `python_homework` folder and virtual environment, do the following:

```bash
pip install plotly
pip install dash
```

For the following code examples, you create programs in the `assignment12` folder of your `python_homework` directory.  Some of this code won't run correctly within the Python interactive shell.

---

## **12.1 Plotting with Pandas**

### **Overview**
Pandas simplifies data visualization by providing built-in plotting methods for DataFrames and Series. These plots are ideal for quick data exploration and basic visualizations.

### **Key Plot Types:**
- **Line Plot:** Displays trends over time or continuous data.
- **Bar Plot:** Used for comparing categorical data.
- **Histogram:** Shows the distribution of numerical data.

### **When to Use These Plots:**
- **Line Plots** are typically used for showing data trends over time, such as sales or stock prices over months.
- **Bar Plots** are ideal when you need to compare quantities between different categories, such as the sales of different products or regions.
- **Histograms** are useful for analyzing the distribution of numerical data, identifying patterns, skewness, or the range of values.

Within the `assignment12` folder of your `python_homework` directory, create `lesson12_a.py`.  This code uses the DataFrame plot() method, which is part of Pandas, but, to actually display the plot, you also need Matplotlib, to do the `show()`.  Your program should contain the following code:

### **Example Code: Plotting with Pandas**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load a dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300]
}
df = pd.DataFrame(data)

# Line Plot
df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")
plt.show()

# Bar Plot
df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
plt.show()
```

Try this out.  The behavior of Matplotlib is like what you saw in the previous lesson.  A graphic window appears, and the program stops to wait at that point, until you close the window.
---

## **12.2 Interactive Visualizations with Plotly**

### **Overview**
Plotly is a powerful library for creating interactive, highly customizable plots. It allows for hover tooltips, zooming, and dynamic interactions that improve user experience.  The code below uses a sample dataset that is provided as part of Plotly, but in the general case, you would use a Pandas DataFrame loaded from a CSV file or database.  Within the `assignment12` folder, create `lesson12_b.py` with the following code:

### **Example Code: Interactive Scatter Plot**
```python
import plotly.express as px
import plotly.data as pldata


df = pldata.iris(return_type='pandas') # Returns a DataFrame.
fig = px.scatter(df, x='sepal_length', y='petal_length', color='species',
                 title="Iris Data, Sepal vs. Petal Length", hover_data=["petal_length"])
fig.write_html("iris.html", auto_open=True)

# Do not try fig.show()!  This sometimes works, but usually it just hangs.
```
Try it out!  The interactive plot comes up in your browser, and you can hover over data points zoom, select, etc.  The HTML file (with lots of embedded JavaScript) can be used in other contexts.exit

### **Key Features of Plotly:**
- **Interactivity:** Hover tooltips, zooming, and panning.
- **Customization:** Wide range of customization options for visual aesthetics and user interaction.

---

## **12.3 Building Dashboards with Dash**

### **Overview**
Dash is a framework for creating interactive web applications in Python. It leverages Plotly for visualizations and allows you to create dashboards that update in real-time based on user input.  When you install Dash, you also install Flask as a dependency.  Flask is a web application server framework, like Node or Rails, but in Python.  When you run a Dash dashboard, the Flask server runs.  Dash pages are dynamic, in that you can add dropdown lists or other controls to affect what is displayed.  Within the `assignment12` folder, create a file `lesson12_c.py, with the following content:

### **Example Code: Simple Dashboard**
```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True)


# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="stock-dropdown",
        options=[{"label": symbol, "value": symbol} for symbol in df.columns],
        value="GOOG"
    ),
    dcc.Graph(id="stock-price")
])

# Callback for dynamic updates
@app.callback(
    Output("stock-price", "figure"),
    [Input("stock-dropdown", "value")]
)
def update_graph(symbol):
    fig = px.line(df, x="date", y=symbol, title=f"{symbol} Price")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 
```

Ok, now run this file.  And, what seems to happen is ... nothing, except the program seems to hang.  But, actually, you have started a web server.  Use your web browser to connect to it, at `http://localhost:8050`.  You see the interactive chart!  At the top, you can select a stock symbol, and you see the corresponding line chart for the stock price.  Sometimes you might have a port conflict, in which case you can specify an alternate port, by adding `port=8055` or some such port to your app.run() statement.

Now, to explain the code above.  This code uses another sample dataset built into Plotly.  That is loaded via the `pldata.stocks()` statement above.  You can find these documented here: [https://plotly.com/python-api-reference/generated/plotly.data.html].  Of course, you could load a CSV file instead.  

To explain the code, a bunch of comments are added below.

```python
from dash import Dash, dcc, html, Input, Output # Dash components you need
import plotly.express as px # Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
import plotly.data as pldata # This is only needed to give access to the Plotly built in datasets.

df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True) # This loads one of the datasets


# Initialize Dash app
app = Dash(__name__) # This creates the app object, to wich various things are added below. 
# __name__ is the name of the running Python module, which is your main module in this case

# Layout: This section creates the HTML components
app.layout = html.Div([ # This div is for the dropdown you see at the top
    dcc.Dropdown( # This creates the dropdown
        id="stock-dropdown", # and it needs an id
        options=[{"label": symbol, "value": symbol} for symbol in df.columns], # This populates the dropdown with the list of stocks
        value="GOOG" # This is the initial value
    ),
    dcc.Graph(id="stock-price") # And the graph itself has to have an ID
])

# Callback for dynamic updates
@app.callback( # OK, now this is a decorator.  Hmm, we haven't talked about decorators in Python.  This decorator is decorating the update_graph() function.
    # Because of the decorator, the update_graph() will be called when the stock-dropdown changes, passing the value selected in the dropdown.
    Output("stock-price", "figure"),  # And ... you get the graph back
    [Input("stock-dropdown", "value")] # When you pass in the value of the dropdown.
)
def update_graph(symbol): # This function is what actually does the plot, by calling Plotly, in this case a line chart of date (which is the index) vs. the chosen stock price.
    fig = px.line(df, df.index, y=symbol, title=f"{symbol} Price")
    return fig

# Run the app
if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
    app.run(debug=True) # start the Flask web server
```

Whew, clear as mud, eh?  You could add other controls to the page, and for each you could cause appropriate changes to the graph.  To understand Dash and Plotly fully, you need to spend time studying the Plotly and Dash documentation, or perhaps by asking your friendly AI how to do this or that.
---

## **12.4 Reflection**

### **Differences Between Static and Interactive Visualizations:**
- **Static Visualizations:** Easier to create and quicker to render but lack user interaction.
- **Interactive Visualizations:** Allow users to explore data, zoom, filter, and interact, providing a deeper and more engaging analysis experience.

### **Advantages of Dashboards:**
- Real-time data exploration and updates.
- User interaction with data (e.g., dropdowns, sliders) enables custom insights.
- Efficient presentation of key metrics in a professional setting.

---

## **Summary**

In this lesson, you learned:
1. How to visualize data directly from Pandas DataFrames.
2. How to create interactive visualizations with Plotly.
3. How to build dynamic dashboards using Dash.
4. The differences between static and interactive visualizations and their real-world applications.

For more details, explore the [Plotly Documentation](https://plotly.com/python/) and [Dash Documentation](https://dash.plotly.com/).

---

### Additional Resources:
1. **Matplotlib Tutorials:** For more detailed Matplotlib tutorials, check out [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html).
2. **Seaborn Gallery:** Explore different plot examples at the [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html).
3. **Data Visualization in Python:** To explore more about data visualization strategies and best practices, visit [Data Visualization in Python](https://realpython.com/python-data-visualization-using-matplotlib/).

