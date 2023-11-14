import pandas as pd
import numpy as np

def import_fiels():

    data_site1 = pd.read_csv('final_projects/Karina0615/Import/Data/Data_SITE-1.csv')
    data_site2 = pd.read_csv('final_projects/Karina0615/Import/Data/Data_SITE-2.csv')
    data_site3 = pd.read_csv('final_projects/Karina0615/Import/Data/Data_SITE-3.csv')
    # Merging 3 tables into one
    df = pd.concat([data_site1, data_site2, data_site3])
    return df


def cleaning_data(df):
        
    # Delete rows if column Data, Name_sate, Country are empty
    df.dropna(axis=0, subset = ['Date', 'Name_sate', 'Country', 'ID_promocode'], inplace=True)

    # Fill other missing values by 0
    df.fillna(0, inplace=True)
    return df

def  convert_dtype(df):
    #Chengin data type
    convert_dict = {"Unique_clients": int,
                    "Registrations": int,
                    "ID_promocode": int}
    return df.astype(convert_dict)
    
def adding_column(df):
    # Calculating Customers convertion after using promocode
    df['Customer_conversion']= round((df["Registrations"] / df['Unique_clients'] * 100), 0)
    # Calculating Total of Unique Customers by Country and Name_sate
    df["Total_unique_clients"]= df.groupby(['Name_sate', 'Country'])['Unique_clients'].transform('sum')
    return df

# Adding nem column with condition
def adding_new_column_based_on_conditions(df, conditions, values, new_column_name):
    df[new_column_name] = np.select(conditions, values) 

files = import_fiels()

clean_data = cleaning_data(files)

#Checking data type in DataFrame
clean_data.info()

df = convert_dtype(clean_data)
print(df.dtypes)

df = adding_column(df)

# Define your conditions and values
conditions_conversion = [
    (df.Customer_conversion <= 30),
    (df.Customer_conversion >= 31) & (df.Customer_conversion <= 60),
    (df.Customer_conversion >= 61) & (df.Customer_conversion <= 100)
]
values_conversion = ["C", "B", "A"]

conditions_promocode = [(df.ID_promocode == 22),
                        (df.ID_promocode == 40),
                        (df.ID_promocode == 15)]
values_promocode = ['holiday', 'party', 'weekend']

# Use the function to assign values
adding_new_column_based_on_conditions(df, conditions_conversion, values_conversion, 'Status')
adding_new_column_based_on_conditions(df, conditions_promocode, values_promocode, 'Name_promocode')

print(df)

# Import all changes to new csv file
d = df.to_csv('final_projects/Karina0615/Export/for_vizualization.csv')
df_new = pd.read_csv('final_projects/Karina0615/Export/for_vizualization.csv')

print(df_new) 

# Promotion Analysis:
def promotion_analysis(df_new):
    # Group the data by 'ID_promocode'
    grouped = df_new.groupby('ID_promocode')
    # Analyze the impact on different metrics
    metrics = ['Unique_clients', 'Registrations', 'Customer_conversion']
    promotion_stats = grouped[metrics].agg(['mean', 'sum'])
    # Identify the most effective promotion based on  criteria, to find the promotion with the highest mean 'Unique_clients':
    most_effective_promotion = promotion_stats['Unique_clients']['mean'].idxmax()
    # Print the statistics
    print(promotion_stats)
    print(f"The most effective promotion for 'Unique_clients' is ID_promocode {most_effective_promotion}")


prom_statistic = promotion_analysis(df_new)