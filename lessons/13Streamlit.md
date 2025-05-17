# Building Interactive Apps with Streamlit

## Lesson Overview

**Learning objective:** Learn to create interactive web applications for data visualization and analysis using Streamlit.

Topics: 
  * Introduction to Streamlit and its benefits
  * Basic Streamlit components and layout
  * Interactive data visualization with Streamlit
  * Deploying Streamlit applications

## What is Streamlit?

Streamlit is a Python library that makes it easy to create custom web apps for machine learning and data science. It turns data scripts into shareable web apps in minutes, not weeks.

### Key Features
* Simple Python-first syntax
* Rich set of UI components
* Easy integration with data science libraries
* Quick deployment options

### Installation and Setup

First, let's set up a virtual environment and install Streamlit:

1. Create a project folder named `streamlit_project`.

2. Open the folder in **VSCode** (recommended) or any IDE of your choice.

3. In the terminal, run:

```bash
# Create a virtual environment
python -m venv .venv
```

4. After creating the virtual environment, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P), search for "Python: Select Interpreter", and choose the .venv environment.
Once selected, VSCode will automatically activate the virtual environment in all new terminals. This removes the need to manually activate it every time.


5. If you're not using VSCode, or prefer manual activation:

# Activate the virtual environment
# For Windows (Git Bash):
```bash
source .venv/Scripts/activate
```

# For macOS/Linux:
```bash
source .venv/bin/activate
```
6. Create requirements.txt file
```bash
streamlit==1.24.0
pandas==1.5.3
plotly==5.15.0
numpy==1.24.3
```
7. Install the dependencies. Run following command in your vs code terminal.
```bash
pip install -r requirements.txt
```

## Basic Streamlit Components
### Text and Data Display

Streamlit provides a variety of methods to render static content such as text, markdown, and code. These elements are useful for building the layout and guiding users through your app.

#### Exercise 1: Text and Data Display
- Create a python script app.py
In this exercise, you will add static content to your app by writing the following code into your app.py file:
```python
import streamlit as st  # Importing the Streamlit library

# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
st.header("Section 1")  # Adds a section header — good for breaking content into parts
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
st.text("Simple text")  # Displays plain, unformatted text — like a basic message
st.markdown("**Bold** and *italic* text")  # Markdown lets you add simple formatting like bold and italics

# Display data
st.write("Automatic data display")  # Streamlit's flexible method — handles strings, numbers, dataframes, and more
st.code("print('Hello World')", language='python')  # Nicely formats code blocks with syntax highlighting
st.latex(r"\int_{a}^{b} x^2 dx")  # Renders LaTeX math formulas — great for equations

```

Once you've saved and run your app.py file using the command:

```bash 
streamlit run app.py
```
Open your browser to http://localhost:8501 to view your app.

Note: Any time you change a value in one of the input components, go to the browser tab and refresh ,Streamlit  reruns the entire script from top to bottom using the updated values. This means your app always reflects the latest state .
You can refresh the tab manually, or use the “Always rerun” option in the top-right of the Streamlit page for instant updates as you code.

#### Exercise - 2
### Data Input Components
```python
# Text input
st.header("Section 2")  # A new section to group interactive input components
name = st.text_input("Enter your name", "John Doe")  # Simple text field with a default value
description = st.text_area("Description", "Write something...")  # Multi-line text box for longer input

# Numeric input
age = st.number_input("Age", min_value=0, max_value=120, value=25)  # Number picker with min/max range
score = st.slider("Score", 0, 100, 50)  # Slider to pick a number in a range — great for ratings or scores

# Selection widgets
option = st.selectbox("Choose an option", ["A", "B", "C"])  # Dropdown menu — user picks one option
options = st.multiselect("Multiple options", ["X", "Y", "Z"])  # Allows multiple selections at once

# Date and time
date = st.date_input("Select date")  # Calendar-style date picker
time = st.time_input("Select time")  # Clock-style time picker

# Buttons and checkbox
if st.button("Click me"):  # A button that runs code when clicked
    st.write("Button clicked!")  # Responds when the button is pressed
    
if st.checkbox("Show/Hide"):  # Checkbox to toggle something on/off
    st.write("Visible content")  # Displays this text only if the box is checked
```
- you can again now refresh your tab in browser to see the updated output.

Note:Unlike dropdowns or sliders (which always keep a selected value), buttons in Streamlit are "stateless" — they don’t hold their state after being clicked. Instead, Streamlit checks whether the button was pressed during that specific run of the script. That’s why we use an if statement with them.

Also, clicking a button triggers a full rerun of the script, just like other controls.

Note: 📍 Where does st.write() show output?
Streamlit renders output in the order the code runs — so the st.write() here appears right under the button. To control placement more precisely, you can use layout elements like columns or placeholders.


## Exercise 3: Layout and Containers
In this section, you’ll learn how to organize your app using columns, expanders, and a sidebar.

Continue working in the same app.py file you created earlier. You can either:
-Append the new code at the bottom of the file



```python
st.header("Section 3")

# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:  # Everything under this goes into the left column
    st.header("Column 1")
    st.write("Content for column 1")

with col2:  # Everything under this goes into the right column
    st.header("Column 2")
    st.write("Content for column 2")

# Expandable sections
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])
```

Streamlit uses the Python with statement to define scoped areas for content. 
```python
with col1:
    st.write("Some content")
```
…it means "put this content inside column 1." Streamlit handles layout placement based on these scopes — it’s a readable way to group content visually.



## Exercise 4: Building a Simple Dashboard

Create a new python script named 'dashboard_app.py'.

```python
import streamlit as st  
import pandas as pd     # Used to work with tabular data
import numpy as np      # Helps generate random numbers
import plotly.express as px  # For interactive charts

# Create sample data — just faking some numbers to simulate a small product dataset
np.random.seed(42)  # Setting a seed so results are consistent every time you run
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': np.random.randint(100, 500, size=4),   # Random sales numbers
    'Profit': np.random.randint(20, 100, size=4)    # Random profit numbers
}
df = pd.DataFrame(sample_data)  # Convert the data into a DataFrame for easy handling

# Sidebar filters — this shows up in the sidebar for user interaction
st.sidebar.header('Filter Options')  # Sidebar title
selected_product = st.sidebar.selectbox('Select Product', df['Product'])  # Dropdown to choose a product

# Filter the data based on the user's selection
filtered_df = df[df['Product'] == selected_product]  # Show only the row that matches the selected product

# Main app content starts here
st.title('Simple Product Dashboard')  # Big title for the dashboard

# Display key numbers using metrics — side-by-side using columns
col1, col2 = st.columns(2)  # Create two columns for layout
with col1:
    st.metric('Sales', f"${filtered_df['Sales'].values[0]:,}")  # Show sales in a pretty format
with col2:
    st.metric('Profit', f"${filtered_df['Profit'].values[0]:,}")  # Show profit similarly

# Add a bar chart comparing all products — gives full context beyond the filter
st.subheader('Sales and Profit Comparison')  # Subheading for the chart
bar_chart = px.bar(df, x='Product', y=['Sales', 'Profit'], barmode='group')  # Grouped bar chart
st.plotly_chart(bar_chart)  # Render the chart in the app
```

in your terminal execute
```bash
streamlit run dashboard_app.py
```
## Conclusion
 You now know how to:
- Create basic Streamlit apps
- Add input forms, layouts, and sidebars
- Build simple dashboards with metrics and charts