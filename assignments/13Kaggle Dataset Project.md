# Capstone Project - Kaggle Data Pipeline

Select one of the following datasets and perform cleaning, aggregation, analysis and visualization, illustrating at least 3 insights gleaned from the data.  Optionally, students can propose an alternative dataset and set of metrics to their CIL by the end of week 13.  The projects are intentionally open-ended in that it is up to the student to decide what they learn from the data, and how it is documented and visualized.

## **Global Superstore**

The [Global Superstore](https://www.kaggle.com/datasets/anandaramg/global-superstore/data) is a collection of sales data from a large retailer.  The goal is to find, document and visualize at least three business insights from the data.

1. **Data Conversion and Cleaning**

Load the data into a ``DataFrame`` using the appropriate delimiter.  Evaluate data quality, looking for issues such as duplicates, null values, and mixed formats.  If these are found, decide whether they signify an issue which needs to be corrected.  Some potential cleaning tasks include:

* Convert dates to ``datetime``
* Strip whitespace
* Unify abbreviations such as state names
* Convert numbers to ``float``

Document the data cleaning performed in a Markdown block

2. **Feature Engineering**

Create at least three additional columns which can be used to derive insights from the data.  For example:

* Columns for just ``year`` and ``month`
* Derive ``Gross Margin`` from ``Profit`` and ``Sales``
* Discretize discounts into buckets such as ``none``, ``low``, ``medium``, ``high``

3. **Aggregation**

Perform at least three aggregations to help drive insights.  For example:

* top/bottom 10 states by total profit
* Category ``Gross Margin``
* ``Customer Lifetime Value`` (``CLV``) - Total profit each customer has generated across all orders

4. **Analyze, Document, and Visualize**

Create at least three plots and associated metrics to illustrate the insights found in the data.
Include ``Markdown`` sections which explain the graphs and analysis.

## **TMDB 5000 Movie Dataset**

The [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv) is a collection of movies with a variety of data about production along with ratings.  The goal is to find the factors which influence critical and financial success.

1. **Data Conversion and Cleaning**

Load the data into a ``DataFrame``.  Evaluate data quality, looking for issues such as duplicates, null values, composite data which could be expanded into additional columns, and mixed formats.  If these are found, decide whether they signify an issue which needs to be corrected.  Some potential cleaning tasks include:

* Convert dates to ``datetime``, year vs date consistency
* Handle null values if necessary
* Numeric conversion e.g. ``revenue`` to ``float``
* Expand/convert ``json`` formated columns, e'g' ``genres``, ``keywords``, ``production companies``
* This is an explanation of the [format](https://www.kaggle.com/code/sohier/tmdb-format-introduction)

Document the data cleaning performed in a Markdown block

2. **Feature Engineering**

Create at least three additional columns which can be used to derive insights from the data.  For example:

* Can be satisfied by expanding ``json`` columns
* Derive ``Gross Margin`` from ``Profit`` and ``Sales``
* Discretize discounts into buckets such as ``none``, ``low``, ``medium``, ``high``

3. **Aggregation**

Perform at least three aggregations to help drive insights.  For example:

* top/bottom 10 directors/actors/studios by rating(average vote)/revenue/budget/profit
* return on investment profit vs budget
* Discretize budgets

4. **Analyze, Document, and Visualize**

Create at least three plots and associated metrics to illustrate the insights found in the data.
Include ``Markdown`` sections which explain the graphs and analysis.  Examples:

* Best ``genres`` for a given success metric
* Impact of particular actors and directors on success metrics
* Genre popularity derived from vote count

## **Life Expectancy (WHO)**

The [Life Expectancy (WHO)](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/data) is a collection of data by country and year with a variety of factors which may impact health.  The goal is to find, document and visualize at least three insights into the factors which influence longevity.

1. **Data Conversion and Cleaning**

Load the data into a ``DataFrame``.  Evaluate data quality, looking for issues such as duplicates, null values, and mixed formats.  If these are found, decide whether they signify an issue which needs to be corrected.  Some potential cleaning tasks include:

* Missing values as blanks or zeros
* Conversion to numeric types
* Unify country names, some appear in different forms
* Outliers

Document the data cleaning performed in a Markdown block

2. **Feature Engineering**

Create at least three additional columns which can be used to derive insights from the data.  For example:

* Adult vs infant mortality
* Discretize factors such as GDP
* Combined vaccination rate

3. **Aggregation**

Perform at least three aggregations to help drive insights.  For example:

* Global life-expectancy trend
* Trends for developing vs developed
* Life expectancy deciles (10 buckets) vs various driving factors

4. **Analyze, Document, and Visualize**

Create at least three plots and associated metrics to illustrate the insights found in the data.
Include ``Markdown`` sections which explain the graphs and analysis.

## **Seattle Airbnb Open Data (2016)**

The [Seattle Airbnb Open Data (2016)](https://www.kaggle.com/datasets/airbnb/seattle/data?select=listings.csv) is a collection of data on Airbnb listing in Seattle.  The goal is to find, document and visualize at least three insights into the factors which influence listing success, or conclusion which can be drawn about Seattle such as desirability or affluence for particular neighborhoods.

1. **Data Conversion and Cleaning**

Load the data into a ``DataFrame``.  Evaluate data quality, looking for issues such as duplicates, null values, and mixed formats.  If these are found, decide whether they signify an issue which needs to be corrected.  Some potential cleaning tasks include:

* Columns with a large percentage of nulls
* Numeric formatting and conversion
* Conversion of ``json``
* Text with html tags

Document the data cleaning performed in a Markdown block

2. **Feature Engineering**

Create at least three additional columns which can be used to derive insights from the data.  For example:

* Derived from ``json`` columns
* revenue per month
* Simplified room type
* Availability ratio

3. **Aggregation**

Perform at least three aggregations to help drive insights.  For example:

* Median price by neighbourhood & simplified room type
* Review score vs. amenity count
* Monthly availability
* 10 most/least affluent neighborhoods and associated profitability

4. **Analyze, Document, and Visualize**

Create at least three plots and associated metrics to illustrate the insights found in the data.
Include ``Markdown`` sections which explain the graphs and analysis.


## Kaggle Project Rubric

* **General Code Quality**

    * [ ]  Code demonstrates a strong understanding of Python basics. 
    * [ ]  Code is well organized and documented with comments.
    * [ ]  Functions are used to structure and organize the code.

* **File Handling and Data Loading**

    * [ ]  Data is loaded from appropriate file formats (CSV, JSON, etc.) using Pandas.
    * [ ]  File paths and loading procedures are clearly defined and handled robustly.
    * [ ]  Demonstrates effective use of Pandas `read_csv()`, `read_json()`, or similar functions.
    * [ ]  Uses `head()`, `tail()`, and `info()` effectively to preview and inspect the data.

* **Data Wrangling and Transformation**

    * [ ]  Demonstrates proficiency in using Pandas for data selection, filtering, and transformation.
    * [ ]  Implements advanced data manipulation techniques, including indexing, slicing, and data type conversion.
    * [ ]  Handles missing data effectively using `dropna()` or `fillna()` with appropriate strategies.
    * [ ]  Identifies and removes duplicate records if necessary using Pandas.
    * [ ]  Code is efficient, well-documented, and follows Pandas best practices.
    * [ ]  At least three extracted features

* **Data Aggregation**

    * [ ]  Uses Pandas `groupby()` function effectively to aggregate data and gain insights.
    * [ ]  Applies a variety of aggregation functions (e.g., `sum()`, `mean()`, `count()`, `min()`, `max()`) to analyze grouped data.
    * [ ]  Clearly presents and interprets the results of data aggregation.
    * [ ]  At least 3 aggregations

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
    * [ ]  At least 3 conclusions supported by charts and text.

* **Reproducibility**

    * [ ]  Provides a well-organized and clearly documented notebook or script that allows others to easily reproduce the entire analysis.
    * [ ]  All dependencies are clearly specified.

When you are ready to submit your Kaggle and Web Scraping projects, use the [final project submission form](https://airtable.com/appoSRJMlXH9KvE6w/shrthD4fozy4UI21I?prefill_Lessons=Python%20100%20v1:%20Lesson%2015%20-%20Project%20Completion%20and%20Presentations).
