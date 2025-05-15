
# **Lesson 11 — Advanced Data Visualization Techniques**

## **Lesson Overview**
**Learning objective:** students will learn how to build advanced, interactive visualizations using Python libraries such as Pandas, Plotly, and Dash. They will practice visualizing data from DataFrames, creating interactive charts, and developing simple dashboards for real-time data exploration. To prepare for the final project, students will complete this lesson and assignment in a personal GitHub repository rather than in `python_homework`. An optional section introduces Streamlit as an alternative to Dash for dashboard development.

### **Topics:**
1. Plotting with Pandas: Visualizing data directly from DataFrames.
2. Interactive Visualizations: Using Plotly for interactive plotting.
3. Dashboards: Creating dynamic dashboards with Plotly and Dash.
4. Advanced Customization: Advanced interactivity, subplots, and real-time updates.
5. Dash and Streamlit compared.

### **Setup**

You are using your own repository, both for the lesson and for the assignment.  If you do the Streamlit portions, these are also to be done within the repository.  The steps are these:

1. Create a folder called  `python-assignment11`.  This should **not** be inside of the `python_homework` folder.  Change to this directory.
2. Do a `git init`.
3. Create a `.gitignore` file.  You can copy the one from `python_homework`, but be sure you know why that one says what it does.
4. Create a virtual environment called `.venv`.  See the README.md for `python_homework` if you don't remember how this is done.
5. Create a `requirements.txt` file.  This should include the following packages.
    - pandas
    - matplotlib
    - plotly
    - seaborn
    - dash
    - gunicorn
    If you do the Streamlit assignment, some further setup is needed.  Note that pandas brings in plotly.  You can specify specific versions of these packages (see the requirements.txt for `python_homework`), but if you don't, you will get the latest version of each of these.
6.  **Important** Activate the virtual environment, with the command:
    ```bash
    source .venv/bin/activate
    ```
    Or, for Windows Git Bash:
    ```bash
    source .venv/Scripts/activate
    ```
    Verify that the virtual environment is active with:
    ```bash
    which python
    ```
    This should return a python location within your python-assignment11 folder.
7. Load the required packages as follows:
    ```bash
    pip install -r requirements.txt
    ```
8. Do `VSCode .`.  Bring up VSCode command palette (Ctrl-Shift-P) and select Python: Select Interpreter.  Select the one with `.venv`.  Close any VSCode terminal sessions and start a new one.  You should see in the command prompt that `.venv` is active.
9. On GitHub, create a new public repository called python-assignment11.  Do not create a README.md or .gitignore or license.  Copy the URL of the repository.  You can use either the HTTL or SSH URL, depending on your preference.  Set the remote for the repository, and push your code.
    ```bash
    git remote add origin <url>
    git add -A
    git commit -m "first commit"
    git push origin main
    ```
10. Create a folder called `assignment11`.  This is for the exercises prior to the assignment.  Create an `assignment11` git branch.

For the following code examples, you create programs in the `assignment11` folder.  Some of this code won't run correctly within the Python interactive shell.  As you do the lesson and assignment, periodically add and commit your changes and push the `assignment11` branch to GitHub.  This is to practice the procedures of a development shop.  When you use these procedures, you can be confident that you won't break something and have to start over.  You can just switch back to the last commit if something breaks.

---

## **11.1 Plotting with Pandas**

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

Within the `assignment11` folder of your `python_homework` directory, create `lesson11_a.py`.  This code uses the DataFrame plot() method, which is part of Pandas, but, to actually display the plot, you also need Matplotlib, to do the `show()`.  Your program should contain the following code:

### **Example Code: Plotting with Pandas**

Create a file called `lesson11_a.py`, with the following content:

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

## **11.2 Interactive Visualizations with Plotly**

### **Overview**
Plotly is a powerful library for creating interactive, highly customizable plots. It allows for hover tooltips, zooming, and dynamic interactions that improve user experience.  The code below uses a sample dataset that is provided as part of Plotly, but in the general case, you would use a Pandas DataFrame loaded from a CSV file or database.  Within the `assignment11` folder, create `lesson11_b.py` with the following code:

### **Example Code: Interactive Scatter Plot**
```python
import plotly.express as px
import plotly.data as pldata


df = pldata.iris(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
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

## **11.3 Building Dashboards with Dash**

### **Overview**
Dash is a framework for creating interactive web applications in Python. It leverages Plotly for visualizations and allows you to create dashboards that update in real-time based on user input.  When you install Dash, you also install Flask as a dependency.  Flask is a web application server framework, like Node or Rails, but in Python.  When you run a Dash dashboard, the Flask server runs.  Dash pages are dynamic, in that you can add dropdown lists or other controls to affect what is displayed.  Within the `assignment11` folder, create a file `lesson11_c.py`, with the following content:

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
app.layout = html.Div([ # This div is for the dropdown you see at the top, and also for the graph itself
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
We'll explain decorators in the next lesson, but here is some additional explanation on the `@app.callback` decorator.  That decorator is provided by Dash and is associated with the app object.  Within your `app.layout`, you can have one or several HTML controls, each with an ID.  In this case, you have just one, the dropdown.  When you use `app.@callback`, the function that follows (the function is update_graph() in this case) will be called any time one of the controls that is specified as an Input for that callback has a change in value, that is, each time the user enters or clicks on something.  The changed value or, in the case of multiple Inputs, the changed values, are then passed to the decorated function.  That function returns the Output, in this case a graph.  (It is also possible to have multiple Outputs for the callback, but that's beyond the scope of this lesson.)  You can have multiple `@app.callback` decorator statements within a Dash program, each decorating a different function.  So, for example, you could have several different graphs on the page, each of which is controlled by a different set of HTML controls.

Whew, clear as mud, eh?  Let's give a summary of how Dash works.

### **A Summary of Dash**

1. The app: You always create an app, with `app = Dash(__name__)`.  This gives you access to `app.layout()` and `@app.callback()`.
2. HTML components: You declare these with `html.something()`.  This is the usual list of html components: div, container, paragraph, whatever, nested as you choose, and styled as you choose.  (Styling is out of scope for this lesson, but there is, for example, a Bootstrap package for Dash.)
3. Dynamic components and controls: You declare these with `dcc.something()`.  These are (a) components you want to modify in response to user input, or (b) controls that catch that user input.  For controls, you have the usual list: radio buttons, dropdowns, input, sliders, tabs, etc.  For components you update, one is `dcc.graph`, but you can update a paragraph or div or whatever you like.  One useful thing to update is a data table, You import dash_table from dash, and then do a `dash_table.DataTable(...)`.  You can create pandas DataFrames, convert them to dicts, and display them in the table.
4. Callbacks.  If you have controls, you will have one or more functions that are decorated with @app.callback.  As follows:
    ```python
    @app.callback(Output(id, what), [Input(id, value), Input(id2, value2), ...])
    update_function(value, value2, ...):
        # logic depending on the values passed
        ...
        return what
    ```
    Let's break this down.  The Output specifies the id of the HTML element to update, and the attribute (what) of that component that is to be changed.  You have a list of one or more inputs, and for each, you have the id of the HTML control and the value it has.  (Note that for a multi-select list, `value` may be a list.)  Any time the value of one of these controls changes as a result of user input, the update_function() will be called so that it can do its thing and return the updated stuff.  Several different update functions might be registered for the same input, so as to update different HTML elements when a particular control or set of controls changes.

That's Dash in a nutshell.  Your homework doesn't include DataTable, but maybe it should, as DataTable provides a way to display DataFrames.  The DataTable works like:

```python
import pandas as pd
import dash_table, Dash, html from dash

app = Dash(__name__)

df = pd.read_csv("some csv file")

app.layout = html.div([dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='tbl')])
```
And you can make the table interactive, for example by having a callback any time a cell is clicked.  

To understand Dash and Plotly fully, you need to spend time studying the Plotly and Dash documentation, or perhaps by asking your friendly AI how to do this or that.

---

## **11.4 Reflection**

### **Differences Between Static and Interactive Visualizations:**
- **Static Visualizations:** Easier to create and quicker to render but lack user interaction.
- **Interactive Visualizations:** Allow users to explore data, zoom, filter, and interact, providing a deeper and more engaging analysis experience.

### **Advantages of Dashboards:**
- Real-time data exploration and updates.
- User interaction with data (e.g., dropdowns, sliders) enables custom insights.
- Efficient presentation of key metrics in a professional setting.

---

## **11.5 Dash and Streamlit**

Streamlit, like Dash, is a way of creating a web based dashboard for data presentation.

Advantages of Dash:
- Widely used
- Gives you a lot of control, all the power that you have in any front end framework
- Better for large complicated projects

Disadvantages of Dash:
- Steep learning curve

Advantages of Streamlit:
- Pretty easy as compared with Dash

Disadvantages:
- Not as widely used
- Doesn't give you quite as much control

For your final project, you will create a dashboard using one of these tools.  Which one you use is up to you.  Check out the optional Streamlit information and assignment if you are interested in Streamlit.

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

