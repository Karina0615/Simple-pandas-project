from pathlib import Path
import pandas as pd
import numpy as np

HERE = Path(__file__).parent
DATA_FOLDER = HERE

diamonds = pd.read_csv(DATA_FOLDER / 'diamonds.csv')
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


print("Include only numeric columns in the diamonds DataFrame.")
numeric_columns = diamonds.select_dtypes(include='number')
diamonds2 = pd.read_csv(DATA_FOLDER / 'diamonds.csv', usecols= numeric_columns )
print(diamonds2.head())