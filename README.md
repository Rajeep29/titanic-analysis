# 🚢 Titanic Survival Analysis using Python

This project performs Exploratory Data Analysis (EDA) on the **Titanic dataset** to understand patterns affecting passenger survival.  
The dataset is loaded directly from Seaborn and cleaned before performing visual and analytical exploration.

---

## 📌 Project Objectives
- Clean and preprocess the Titanic dataset
- Analyze how different factors affected survival:
  - Gender
  - Passenger class (Pclass)
  - Age
  - Family size

---

## 🧠 Skills & Techniques Used
- **Data Cleaning**
  - Handling missing values (`fillna`, `dropna`)
  - Changing datatypes
  - Feature engineering (Family size = sibsp + parch + 1)

- **Exploratory Data Analysis**
  - Grouping and calculating survival percentage
  - Insights based on gender, class, age, and family size

- **Data Visualization**
  - `countplot`
  - `histplot`
  - `kdeplot`
  - `heatmap`
  - Stacked bar plots

---

## 🛠️ Technologies & Libraries Used
| Library | Purpose |
|---------|---------|
| Pandas | Data handling & preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical plots |

---

## 📊 Key Findings (Insights)
- **Females had a much higher survival rate** than males.
- **1st-class passengers survived more** compared to 2nd and 3rd class.
- Survival chances varied based on **age distribution**.
- People with very large families had a **lower survival rate**, while smaller families survived more.

---


