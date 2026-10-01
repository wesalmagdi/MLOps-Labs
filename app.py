import pandas as pd

file_path = input("Enter the CSV file path: ")

df = pd.read_csv(file_path)

print(df.head(3))
