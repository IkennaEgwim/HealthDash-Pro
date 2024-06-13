import os
import pandas as pd
from datetime import datetime

def data_collection():
    """
    Description: This function will read multiple csv files in a list of dataframes. 

    Args: The function takes no argument.

    Return: The function returns a list of dataframes    
    """
    dfs = []
    directory = r"C:\Users\ernes\Downloads\HealthDash-Pro\dataset"
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_source = filename.split('.')[0]
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            df['file_source'] = file_source
            dfs.append(df)
    return dfs
df_lists = data_collection()
cause_of_deaths_df = df_lists[0]
diabetes_1_df = df_lists[1]
diabetes_2_df = df_lists[2]
health_failure_df = df_lists[3]
liver_disease_df = df_lists[4]
kidney_disease_1_df = df_lists[5]
kidney_disease_2_df = df_lists[6]


#print(df_lists[6].info())
print(cause_of_deaths_df.info())


