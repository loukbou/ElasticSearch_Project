import pandas as pd

# lire le CSV
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", dtype=str)

# convertir la colonne Date
df['Date'] = pd.to_datetime(df['Date'], format='%m%d%Y', errors='coerce')

# formater en yyyy-MM-dd
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# sauvegarder CSV prêt pour ingestion
df.to_csv("squirrel_fixed.csv", index=False)
