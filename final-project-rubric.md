# I. Kaggle Project Rubric

### Project Description
Students will create a Kaggle notebook that loads CSV files from one or several datasets. These may be datasets that are publicly available on Kaggle, or they might be datasets the students have uploaded to Kaggle for the purpose of the project. The project should demonstrate data cleaning, data organization, and data presentation, showing interesting correlations or insights to be learned from the data, and demonstrating those correlations or insights with tables, charts, and graphs.

### Project Evaluation

* **Lesson 01 & 02: Python Fundamentals and Data Structures**

    * [ ]  Code demonstrates a strong understanding of Python basics. Variables, data types, operators, control flow (if/else, loops), and functions are used correctly and efficiently.
    * [ ]  Data structures (lists, tuples, dictionaries, sets) are implemented appropriately for the task.
    * [ ]  Code is well-organized, commented, and easy to debug. Error handling (try/except) is implemented to prevent crashes.

* **Lesson 02 & 03: File Handling and Data Loading**

    * [ ]  Data is loaded from appropriate file formats (CSV, JSON, etc.) using Pandas.
    * [ ]  File paths and loading procedures are clearly defined and handled robustly.
    * [ ]  Demonstrates effective use of Pandas `read_csv()`, `read_json()`, or similar functions.
    * [ ]  Implements error handling for file operations (e.g., file not found).
    * [ ]  Uses `head()`, `tail()`, and `info()` effectively to preview and inspect the data.

* **Lesson 04 & 05: Data Wrangling and Transformation**

    * [ ]  Demonstrates proficiency in using Pandas for data selection, filtering, and transformation.
    * [ ]  Implements advanced data manipulation techniques, including indexing, slicing, and data type conversion.
    * [ ]  Handles missing data effectively using `dropna()` or `fillna()` with appropriate strategies.
    * [ ]  Identifies and removes duplicate records using Pandas.
    * [ ]  Code is efficient, well-documented, and follows Pandas best practices.

* **Lesson 04: Data Aggregation**

    * [ ]  Uses Pandas `groupby()` function effectively to aggregate data and gain insights.
    * [ ]  Applies a variety of aggregation functions (e.g., `sum()`, `mean()`, `count()`, `min()`, `max()`) to analyze grouped data.
    * [ ]  Clearly presents and interprets the results of data aggregation.

* **Visualization Quality**

    * [ ]  Creates multiple (3+) high-quality, informative, and visually appealing visualizations using appropriate libraries (e.g., Matplotlib, Seaborn, Plotly).
    * [ ]  Visualizations are clear, concise, and easy to understand, with appropriate titles, labels, legends, and color schemes.
    * [ ]  Demonstrates strong understanding of design principles.
    * [ ]  Provides clear explanations of the insights conveyed by each visualization.

* **Chart Types and Interpretation**

    * [ ]  Uses a diverse range of chart types (e.g., scatter plots, bar charts, histograms, box plots, heatmaps) to provide a comprehensive view of the data.
    * [ ]  Demonstrates a clear understanding of the strengths and weaknesses of each chart type and selects them strategically.
    * [ ]  Provides insightful interpretations of the visualizations, connecting them to the data analysis and the problem domain.

* **Dataset and Feature Understanding**

    * [ ]  Uses a dataset that is appropriate for the analysis.
    * [ ]  Demonstrates a clear understanding of the dataset's characteristics, limitations, and potential biases.
    * [ ]  Selects and uses a sufficient number of relevant features to support a meaningful analysis.

* **Conclusions and Insights**

    * [ ]  Provides a clear, concise, and insightful summary of the project's key findings and conclusions.
    * [ ]  Connects the findings to the original problem or question and discusses their implications.
    * [ ]  Identifies potential limitations of the analysis.
    * [ ]  Demonstrates a strong understanding of the data's story and effectively communicates it.

* **Reproducibility**

    * [ ]  Provides a well-organized and clearly documented notebook or script that allows others to easily reproduce the entire analysis.
    * [ ]  All dependencies are clearly specified.
    * [ ]  Provides a downloadable result (e.g., CSV file) in an appropriate format.

# II. Local Project Rubric

* **Web Scraping**

    * [ ] Uses appropriate libraries (Selenium) to retrieve data from the web
    * [ ] Handles common scraping challenges like missing tags, pagination, and user-agent headers
    * [ ] Saves raw data in a structured format such as .csv or .json
    * [ ] Avoids scraping duplication or redundant requests

* **Data Cleaning & Transformation**

    * [ ] Loads raw data into a Pandas DataFrame or equivalent structure
    * [ ] Cleans missing, duplicate, or malformed entries effectively
    * [ ] Applies appropriate transformations, groupings, or filters
    * [ ] Shows before/after stages of cleaning or reshaping

* **Data Visualization**

    * [ ] Includes at least three visualizations using Plotly, Streamlit, or Dash
    * [ ] Visuals are relevant, well-labeled, and support the data story
    * [ ] User interactions such as dropdowns or sliders are implemented
    * [ ] Visualizations respond correctly to user input or filters

* **Dashboard / App Functionality**

    * [ ] Built with Streamlit or Dash to display data and insights
    * [ ] Features clean layout and responsive components
    * [ ] Allows users to explore different aspects of the data
    * [ ] Provides clear titles, instructions, and descriptions for user guidance

* **Code Quality & Documentation**

    * [ ] Code is well-organized and split into logical sections or functions
    * [ ] Inline comments or markdown cells explain major steps or choices
    * [ ] All dependencies are listed and environment setup is reproducible
    * [ ] Comments or markdown cells explain logic
    * [ ] `README.md` includes summary, setup steps, and a screenshot