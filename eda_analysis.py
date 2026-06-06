import pandas as pd

# Load dataset
df = pd.read_csv("books_dataset.csv")

print("===== First 5 Rows =====")
print(df.head())

print("\n===== Dataset Information =====")
print(df.info())

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Number of Books =====")
print(len(df))

print("\n===== Rating Distribution =====")
print(df["Rating"].value_counts())

print("\n===== Price Statistics =====")
print(df["Price"].describe())

print("\n===== Most Common Rating =====")
print(df["Rating"].mode()[0])