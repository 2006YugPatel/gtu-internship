import pandas as pd

# Load the dataset
df = pd.read_csv("Renewable_Energy_Data.csv")

# Display the first 5 rows
print(df.head())
# Dataset Shape
print("\nShape of Dataset:")
print(df.shape)

# Column Names
print("\nColumns:")
print(df.columns)

# Information
print("\nInformation:")
print(df.info())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values

for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Insight:
# No missing values were found, so no changes were required.

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))

numeric_df = df.select_dtypes(include="number")

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

# Insight:
# The heatmap shows relationships between numerical features.

numeric_df.hist(figsize=(12,8))

plt.tight_layout()
plt.show()

# Insight:
# Histograms show the distribution of numerical columns.

plt.figure(figsize=(8,5))

sns.boxplot(data=numeric_df)

plt.xticks(rotation=45)

plt.show()

# Insight:
# Boxplots help identify outliers.

plt.figure(figsize=(6,4))

sns.countplot(x="Energy_Source", data=df)

plt.title("Energy Source Count")

plt.show()

# Insight:
# Shows the number of records for each energy source.

sns.pairplot(df, hue="Energy_Class")

plt.show()

# Insight:
# Pairplot shows relationships between numerical columns grouped by Energy_Class.

df["Weather_Score"] = (
    df["Temperature_C"]
    + df["Solar_Radiation_kWh_m2"]
    - df["Rainfall_mm"]
)

print(df.head())

# Insight:
# Weather_Score combines weather-related features into one new feature.

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

categorical_columns = ["Region","Energy_Source","Season","Energy_Class"]

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

print(df.head())

# Insight:
# Label Encoding converts text into numerical values.


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

numerical_columns = [
    "Temperature_C",
    "Wind_Speed_m_s",
    "Solar_Radiation_kWh_m2",
    "Rainfall_mm",
    "Efficiency_Ratio",
    "Lagged_Production_MWh",
    "Combined_Weather_Index",
    "Weather_Score"
]

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

print(df.head())

# Insight:
# Scaling standardizes numerical values so they are on a similar scale.

# ===============================
# Final Insights
# ===============================

# 1. Dataset contains 1000 records and 11 original features.
# 2. No missing values were found.
# 3. Numerical columns describe weather and production.
# 4. Categorical columns describe region, season, energy source and energy class.
# 5. Correlation heatmap helped identify relationships among numerical features.
# 6. Histograms showed the distribution of numerical data.
# 7. Boxplots helped check for outliers.
# 8. Countplot showed the frequency of each energy source.
# 9. Pairplot showed relationships among features.
# 10. Label Encoding converted categorical values into numbers.
# 11. Standard Scaling normalized numerical columns.
# 12. A new Weather_Score feature was created to combine weather information.