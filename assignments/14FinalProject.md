# Lesson 14 — Web Scraping and Dashboard Project

## Lesson Overview
In this lesson, students will create **four distinct programs** that retrieve baseball history data from the **Major League Baseball History** website and display the results in an interactive dashboard. The project will involve **Selenium** for web scraping, data cleaning, transforming the data into a structured format, storing it in a MySQL database, querying it via command line, and presenting it using **Streamlit** or **Dash** with interactive visualizations.

**Learning Objective:**  
By completing this project, students will:
- Use **Selenium** to scrape data from a website.
- Clean and transform the raw data into a structured format.
- Store the data in a **MySQL** database, with each CSV file as a separate table.
- Query the database using **joins** via command line.
- Build an interactive dashboard using **Streamlit** or **Dash** to display the insights.

## Projects

### 1. **Web Scraping Program**  
- **Goal**: Scrape data from [Major League Baseball History](https://www.baseball-almanac.com/yearmenu.shtml).
- **Steps**:
  - Use **Selenium** to retrieve the data.
  - Extract relevant details (year, event names, statistics).
  - Save the raw data into **CSV** format for each dataset.
  - Handle challenges such as:
    - Pagination
    - Missing tags
    - User-agent headers for mimicking a browser request.

### 2. **Database Import Program**  
- **Goal**: Import the CSV files into a **MySQL** database.
- **Steps**:
  - Create a program that imports each CSV as a separate table in the database.
  - Ensure proper data types (numeric, date, etc.) during the import.
  - Check for errors during the import process.

### 3. **Database Query Program**  
- **Goal**: Query the database via the command line.
- **Steps**:
  - Allow users to run queries, including at least **joins** (e.g., combining player stats with event data).
  - Ensure the program can handle flexible querying, allowing for filtering by year, event, or player statistics.
  - Handle errors and display results appropriately.

### 4. **Dashboard Program**  
- **Goal**: Build an interactive dashboard using **Streamlit** or **Dash**.
- **Steps**:
  - Display insights from the data using at least three visualizations.
  - Implement interactive features like:
    - Dropdowns to select years or event categories.
    - Sliders to adjust the data view.
  - Dynamically update the visualizations based on user input.
  - Deploy the dashboard on **Render** or **Streamlit.io** for public access.

All four programs will be included in the **GitHub** repository, and the dashboard will be deployed for public access.

## Data Sources

Students will scrape data from the **[Major League Baseball History Site](https://www.baseball-almanac.com/yearmenu.shtml)**. This site contains historical data such as notable events, player statistics, and achievements year by year.

---

## **Rubric for Lesson 14 - Web Scraping and Dashboard Project**

### **Web Scraping**
- Uses **Selenium** to retrieve data from the web.
- Handles common scraping challenges like missing tags, pagination, and user-agent headers.
- Saves raw data as a **CSV**.
- Avoids scraping duplication or redundant requests.

### **Data Cleaning & Transformation**
- Loads raw data into a **Pandas DataFrame**.
- Cleans missing, duplicate, or malformed entries effectively.
- Applies appropriate transformations, groupings, or filters.
- Shows before/after stages of cleaning or reshaping.

### **Data Visualization**
- Includes at least three visualizations using **Streamlit** or **Dash**.
- Visuals are relevant, well-labeled, and support the data story.
- User interactions such as dropdowns or sliders are implemented.
- Visualizations respond correctly to user input or filters.

### **Dashboard / App Functionality**
- Built with **Streamlit** or **Dash** to display data and insights.
- Features clean layout and responsive components.
- Allows users to explore different aspects of the data.
- Provides clear titles, instructions, and descriptions for user guidance.

### **Code Quality & Documentation**
- Code is well-organized and split into logical sections or functions.
- Inline comments or markdown cells explain major steps or choices.
- All dependencies are listed and environment setup is reproducible.
- Comments or markdown cells explain logic.
- **README.md** includes summary, setup steps, and a screenshot.

---

## **Submission Instructions:**
When you are ready to submit your Kaggle and Webscraping projects, use the [link for the final project submission form](https://airtable.com/appoSRJMlXH9KvE6w/shrthD4fozy4UI21I?prefill_Lessons=Python%20100%20v1:%20Lesson%2015%20-%20Project%20Completion%20and%20Presentations).

1. **Submit the Github Link**: Submit the link to your GitHub repository with all code files, data files, and the **README.md**.
2. **Final Project Presentation**: Provide a brief explanation of your dashboard functionality and insights during the presentation. Submit your video link in the form.

