# CTD_Assignment_14: Build and Deploy a Streamlit Dashboard

## Overview
This assignment is to be implemented using **Streamlit**.  
You will **import a dataset**, **build a dashboard**, **visualize insights**, **showcase data cleaning**, and **deploy your app** to **Streamlit Community Cloud**.

### Requirements
- Import a dataset that has already been cleaned and prepared
- Explain what cleaning and preparation was done
- Visualize key insights through interactive dashboards
- Deploy your app using Streamlit Community Cloud

## Task 1: Project Setup

1. Create a new folder for your project on your local machine.

2. Initialize a Git repository inside this folder:
```bash
git init
```

3. Create a .gitignore file and make sure it includes:
```bash
.venv/
__pycache__/
*.pyc
.DS_Store
```

4. Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
.venv\Scripts\activate     # on Windows
```

5. Install necessary libraries:
```bash
pip install streamlit pandas matplotlib plotly
```

6. Create a Python file named `streamlit_app.py` in your project folder.
   This is the main script Streamlit will run when deploying your app.

## Task 2: Build Your Streamlit Dashboard

### Required Components

1. **Title and Description**
   - Use `st.title()` and `st.markdown()` to introduce your dashboard

2. **Dataset Overview**
   - Import your cleaned dataset using Pandas
   - Display the dataset using `st.dataframe()` or `st.write()`
   - Optionally, summarize with `.describe()` or key statistics

3. **Data Cleaning Summary**
   - Briefly describe what cleaning steps you performed
   - Optional: Show comparison table (raw vs cleaned)

4. **Visualizations**
   - Include at least two interactive charts
   - Examples: bar chart, pie chart, line chart, scatter plot, histogram
   - Use Streamlit's built-in charts or libraries like Plotly/Matplotlib


## Task 3: Deploy Your App
1. Create a **GitHub repository** and push your code:
   - Log in to your GitHub account and create a new repository.
   - Copy the repository URL.
   - Link your local project folder to the GitHub repository:
     ```bash
     git remote add origin <repository-url>
     ```
   - Add and commit your changes:
     ```bash
     git add .
     git commit -m "Initial commit"
     ```
   - Push your code to the GitHub repository:
     ```bash
     git branch -M main
     git push -u origin main
     ```
2. Deploy to **Streamlit Community Cloud**:
   - Visit [Streamlit Cloud](https://streamlit.io/cloud) and log in with your Streamlit account. If you don't have an account, create one using your email or GitHub credentials.

   - Click on the **"New App"** button to start the deployment process.

   - In the **"Select a repository"** section:
      - Connect your GitHub account if you haven't already.
      - Choose the repository where your Streamlit app code is stored.

   - In the **"Branch"** dropdown, select the branch containing your code (usually `main`).

   - In the **"Main file path"** field, specify the path to your Streamlit app file (e.g., `streamlit_app.py`).

   - Click **"Deploy"** to start the deployment process.

   - Wait for the deployment to complete. Once done, you will see a URL where your app is hosted.

   - Test your app by visiting the provided URL to ensure everything works as expected.

   - If you need to make updates to your app, push the changes to your GitHub repository. Streamlit Cloud will automatically redeploy your app with the latest changes.
3. Verify your app loads successfully and is publicly accessible

## Task 4: Submit Your Assignment

### Required Submissions
- Your **Streamlit Community Cloud app URL** (deployment link)
- Your **GitHub repository URL**

### Resources
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

### Example Submissions
1. Canada Dashboard:
   - App: https://canada.streamlit.app/
   - Code: https://github.com/parker84/canada-dashboard

2. Dashboard v2:
   - App: https://dash-board.streamlit.app/
   - Code: https://github.com/dataprofessor/dashboard-v2