# EduPro: Learner Demographics and Course Enrollment Behavior Analysis

## 📌 Project Overview

**EduPro – Learner Demographics and Course Enrollment Behavior Analysis** is a data analytics project that explores learner demographics, course enrollment patterns, and online learning behavior on an educational platform.

The project uses Python and data analysis libraries to process learner, course, and transaction data. It identifies popular courses, analyzes enrollment trends, compares course preferences across age groups and genders, and examines transaction amounts.

An interactive dashboard developed using **Streamlit and Plotly** allows users to explore the data through charts, filters, key performance indicators (KPIs), and downloadable reports.

## 🎯 Project Objectives

- Analyze learner demographics, including age and gender distribution.
- Identify the most popular courses and course categories.
- Compare free and paid course enrollment patterns.
- Examine enrollment behavior across different age groups and genders.
- Analyze monthly enrollment trends and transaction amounts.
- Compare course ratings across categories.
- Explore the relationship between course prices and enrollment counts.
- Build an interactive dashboard for data exploration and reporting.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data cleaning, manipulation, and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive charts and visualizations |
| Streamlit | Interactive web dashboard |
| Google Colab | Data analysis and experimentation |
| Git and GitHub | Version control and project hosting |

## 📂 Dataset Description

The project uses three datasets from the EduPro online learning platform.

### 1. Users

Contains learner information.

- `UserID`
- `UserName`
- `Age`
- `Gender`
- `Email`

### 2. Courses

Contains course information.

- `CourseID`
- `CourseName`
- `CourseCategory`
- `CourseType`
- `CourseLevel`
- `CoursePrice`
- `CourseDuration`
- `CourseRating`

### 3. Transactions

Contains enrollment and transaction information.

- `TransactionID`
- `UserID`
- `CourseID`
- `TransactionDate`
- `Amount`
- `PaymentMethod`
- `TeacherID`

The Teachers sheet is excluded from the analysis.

### Dataset Summary

| Dataset | Number of Records |
|---|---:|
| Users | 3,000 |
| Courses | 60 |
| Transactions | 10,000 |

The three datasets are integrated using `UserID` and `CourseID` to create a combined dataset for analysis.

## ⚙️ Project Workflow

### Phase 1: Dataset Understanding
- Examined the structure and columns of the datasets.
- Identified the information available in each dataset.

### Phase 2: Data Cleaning and Validation
- Checked for missing values and duplicate transaction IDs.
- Validated user and course references.
- Checked course prices, transaction amounts, course durations, and ratings.

### Phase 3: Data Integration and Feature Engineering
- Combined users, courses, and transactions.
- Created age groups for demographic analysis.
- Extracted enrollment month, year, and month name from transaction dates.

### Phase 4: Learner Demographic Analysis
- Analyzed the age distribution of learners.
- Compared the number of male and female learners.
- Examined learner distribution across age groups.

### Phase 5: Course Enrollment Analysis
- Identified popular courses and categories.
- Compared free and paid course enrollment records.
- Analyzed enrollment across beginner, intermediate, and advanced courses.

### Phase 6: Demographic Preferences and Behavior
- Compared course category preferences across age groups.
- Examined category enrollment patterns by gender.
- Compared free and paid enrollment patterns across age groups.

### Phase 7: Data Visualization and Findings
- Created charts for monthly enrollment trends.
- Analyzed monthly transaction amounts.
- Compared average course ratings across categories.
- Examined the relationship between course prices and enrollment counts.

### Phase 8: Interactive Streamlit Dashboard
- Developed an interactive dashboard.
- Added sidebar filters and KPI metrics.
- Integrated charts for demographic and enrollment analysis.
- Added advanced analytics visualizations.

### Phase 9: Data Export and Automatic Insights
- Added a filtered data table.
- Implemented CSV download functionality.
- Generated automatic insights based on the selected data.

## 📊 Dashboard Features

### Key Performance Indicators (KPIs)
- Total unique learners
- Total courses
- Total enrollment records
- Total transaction amount

### Interactive Filters
Users can filter the dashboard by:

- Age group
- Gender
- Course category
- Course type

The dashboard updates its visualizations and insights according to the selected filters.

### Visualizations
- Learner age distribution
- Gender distribution
- Top 10 popular courses
- Enrollment by course category
- Free versus paid course enrollment
- Monthly enrollment trends
- Average course rating by category
- Monthly transaction amount
- Enrollment by course level

### Additional Features
- Dynamic insights and findings
- Filtered enrollment data table
- CSV download for filtered records

## 🔍 Key Findings

The analysis produced the following observations from the dataset:

- The dataset contains **3,000 unique learners**, 60 courses, and 10,000 transaction records.
- Learners aged 26–35 form the largest age group, accounting for approximately 48.20% of unique learners.
- Female learners account for approximately 50.67% of unique learners, while male learners account for 49.33%.
- **Deep Learning** has the highest number of enrollment records among individual courses, with 334 records.
- **Data Science** is the leading course category, with 916 enrollment records.
- Free courses account for approximately 64.03% of enrollment records, compared with 35.97% for paid courses.
- June has the highest monthly enrollment count, with 899 records, while October has the lowest, with 762 records.
- The correlation between course price and enrollment count is approximately -0.163, indicating a weak negative linear relationship in this dataset.

These findings describe the available dataset and do not establish causal relationships between learner characteristics, course prices, and enrollment behavior.
