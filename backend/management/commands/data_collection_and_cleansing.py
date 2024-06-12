import os
import pandas as pd

def data_collection():
    """
    
    """
    dfs = []
    directory = r"C:\Users\admin\Desktop\on-going-projects\HealthDash-Pro\dataset"
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
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


