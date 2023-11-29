from pathlib import Path
import pandas as pd
import numpy as np

HERE = Path(__file__).parent
DATA_FOLDER = HERE

diamonds = pd.read_csv(DATA_FOLDER / 'diamonds.csv', usecols=["carat","cut","color","clarity","depth","table","price","x","y","z"])
#The first 5 rows
print("Print  the first 5 rows")
print(diamonds.head(10))

# use_cols = ["carat", "cut", "x", "y", "z"]
# print("Print with choose column")
# print(diamonds[use_cols].head(6))

# #select a series from diamonds DataFrame. Print the content of the series.
# print("Print one Series")
# print(diamonds["carat"].head(6))

# diamonds["Quality-color"] = diamonds.cut + ", " + diamonds.color
# print("Print with new column")
# print(diamonds.head(6))

# print("Number of rows and columns:")
# print(diamonds.shape)
# print("\nData type of each column:")
# print(diamonds.dtypes)

# print("Summarize of 'object' columns:")
# print(diamonds.describe(include=['object']))

# print("\nAfter renaming two of the columns of the said dataframe:")
# diamonds.rename(columns={'color':'diamond_color', 'clarity':'dimaond_clarity'}, inplace=True)
# print(diamonds.head())

# print("\nRemove the second column of the said Dataframe:")
# diamonds.drop('cut', axis=1, inplace=True)
# print(diamonds.head())

# print("\nSort the 'cut' Series in ascending order")
# result = diamonds.cut.sort_values(ascending=True)
# print(result)

# print("\nSort the 'price' Series in descending order")
# result = diamonds.price.sort_values(ascending=False)
# print(result)

# print("\nSort the entire diamonds DataFrame by the 'carat' Series in ascending order")
# result = diamonds.sort_values('carat')
# print(result)

# print("\nSort the entire diamonds DataFrame by the 'carat' Series in descending  order")
# result = diamonds.sort_values('carat', ascending=False)
# print(result)

# print("\nRows to only show carat weight at least 0.3:")
# condition = diamonds["carat"] >= 0.3
# filtered_df = diamonds[condition]
# print(filtered_df.head(10))

# print("\nDiamonds where length>5, width>5 and depth>5:")
# result = diamonds[(diamonds.x>5) & (diamonds.y>5) & (diamonds.z>5)]
# print(result.head())

# print("\nDiamonds that are either Premium or Ideal.")
# result = diamonds[(diamonds.cut == "Ideal") | (diamonds.cut == "Premium")]
# print(result.head())

# print("\nDiamonds that are with a Fair or Good or Premium..")
# result = diamonds[diamonds.cut.isin(['Fair', 'Good', 'Premium'])]
# print(result.head())

# print("\nDisplay all column labels of diamonds DataFrame.")
# print(diamonds.columns)

# print("\nIterate through diamonds DataFrame:")
# for index, row in diamonds.iterrows():
#     print(index, row.carat, row.cut, row.color, row.price)

# print("Drop all non-numeric columns from diamonds DataFrame.")
# numeric_columns = diamonds.select_dtypes(include='number')
# diamonds.drop(columns=numeric_columns, inplace=True)
# print(diamonds.head())

# print("Include only numeric columns in the diamonds DataFrame.")
# numeric_columns = diamonds.select_dtypes(include='number')
# diamonds2 = pd.read_csv(DATA_FOLDER / 'diamonds.csv', usecols= numeric_columns )
# print(diamonds2.head())

# print("List of data types to only describe certain types:")
# print(diamonds.describe(include=['object', 'float64']))

# print("Calculate the mean of each numeric column of diamonds DataFrame")
# print(diamonds.mean(axis=0, numeric_only=True))

# print("Calculate the mean of each row of diamonds DataFrame.")
# print(diamonds.mean(axis=1, numeric_only=True))

# print("Calculate the mean of price for each cut of diamonds DataFrame.")
# grouped = diamonds.groupby('cut')
# print(grouped["price"].mean())
# print(diamonds.groupby('cut').price.mean())

# print("Calculate count, minimum, maximum price for each cut of diamonds DataFrame.")
# grouped = diamonds.groupby('cut')
# print(grouped["price"].agg(["count", "min", "max"]))
# print(diamonds.groupby('cut').price.agg(["count", "min", "max"]))

# print("Side-by-side bar plot of the diamonds DataFrame:")
# grouped = diamonds.groupby('cut')
# means = grouped.price.mean()
# plot = means.plot(kind= "bar")

# print("Count how many times each value in cut series of diamonds DataFrame occurs.")
# grouped = diamonds.groupby('cut')
# print(diamonds.groupby('cut').cut.count())
# #or
# print(diamonds.cut.value_counts())

# print("Display percentages of each value of cut series occurs in diamonds DataFrame.")
# print(diamonds.cut.value_counts(normalize=True))

# print("Display the unique values in cut series of diamonds DataFrame:")
# print(diamonds.cut.unique())

# print("Number of unique values in cut series of diamonds DataFrame:")
# print(diamonds.cut.nunique())

# print("Cross-tabulation of two Series of diamonds DataFrame:")
# print(pd.crosstab(diamonds.cut, diamonds.price))

# print("Various summary statistics of diamonds DataFrame:")
# print(diamonds.cut.describe())
# print(diamonds.carat.describe())

# print("DataFrame of Missing Values (True if missing, False if not missing):")
# missing_values = diamonds.isna()
# missing_values2 = diamonds.isnull()
# print(missing_values.head(10))
# print(missing_values2.head(10))

# print("Count the number of missing values in each Series of diamonds DataFrame.")
# print(diamonds.isna().sum())

# print("Check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame.")
# print("Number of rows and columns:")
# print(diamonds.shape)
# print("After droping those rows where values are missing:")
# print(diamonds.dropna(how='any').shape)

print("New Dataframe:")
diamonds.set_index('color', inplace=True)
print(diamonds.head())