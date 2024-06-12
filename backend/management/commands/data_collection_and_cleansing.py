import os
import pandas as pd

dfs = []
directory = r"C:\Users\admin\Desktop\on-going-projects\HealthDash-Pro\dataset"
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        dfs.append(df)
        print(dfs)