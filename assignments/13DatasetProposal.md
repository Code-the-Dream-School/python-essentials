# Final Assignment Dataset Proposal

## Dataset 1 Information

### 1. Dataset Link
- Original source: https://www.kaggle.com/johndddddd/customer-satisfaction
- Cleaned version: https://www.kaggle.com/teejmahal20/airline-passenger-satisfaction

### 2. Dataset Size
- Training set: 100,000 rows × 24 columns
- Testing set: 26,000 rows × 24 columns

### 3. Data Cleaning and Visualization

#### Data Cleaning:
- ✓ Dropped redundant columns ('id', 'Unnamed: 0')
- ✓ Handled missing values in 'Arrival Delay in Minutes' (filled with 0)
- ✓ Created age groups (1: 0-39, 2: 40-60, 3: 61-100)
- ✓ Label encoded categorical variables:
  - Class
  - Type of Travel
  - Customer Type
  - Gender
  - Age groups

#### Key Visualizations:

##### Demographics:
- Gender distribution (balanced)
- Age distribution (majority 20-60)
- Customer type (more loyal customers)
- Travel type (business vs personal)

##### Satisfaction Analysis:
- By travel class (Business class higher satisfaction)
- By travel type (Business travelers more satisfied)
- By age groups (39-60 age group shows higher satisfaction)

##### Service Ratings:
- WiFi service correlation
- Seat comfort analysis
- Food and drink service
- Online boarding experience


##  Dataset 2 Information
### 1. Dataset Link
- https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers


### 2. Dataset Size
-  10,000 rows
- 18 features

### 3. Data Cleaning and Visualization

- Data cleaning includes handling categorical variables, outlier treatment (1.5 IQR method), and feature scaling using StandardScaler
- Visualizations include:
- Categorical variable distributions
- Scatter plots for transaction counts vs amounts
- Average utilization and revolving balance analysis


## Dataset 3 Information
### 1. Dataset Link
- https://www.kaggle.com/competitions/nlp-getting-started/data?select=train.csv

### 2. Dataset Size
- 10000 rows
- 5 features

### 3. Data Cleaning Tasks:
Handle Missing Values:
keyword column has missing values
location column has significant missing values
Consider either filling with mode values or creating a "missing" category
Text Preprocessing:
Remove punctuations
Remove HTML tags and emojis
Convert text to lowercase
Remove URLs
Remove special characters
Handle hashtags
Tokenization
Remove stop words
Lemmatization/Stemming

### Visualization Suggestions:

Bar plot of target distribution (disaster vs non-disaster)
Word cloud for disaster and non-disaster tweets
Distribution of tweet lengths
Top keywords frequency plot
Bar plot of most common keywords
Correlation between keywords and target variable
Keyword distribution across disaster/non-disaster tweets

N-gram frequency plots
Common words in disaster vs non-disaster tweets
Sentiment distribution


##  Dataset 4 Information

### 1. Dataset Link
-  [Amazon Products Dataset](https://www.kaggle.com/datasets/nguyenngocphung/10000-amazon-products-dataset)

### 2. Dataset Size
- 10,005 rows × 14 columns

### 3. Data Cleaning and Visualization
- Clean nulls in product descriptions/reviews
- Normalize category labels
- Remove duplicates


- Product distribution by category
- Rating histograms
- Word clouds from product descriptions