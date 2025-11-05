# This file was made with the use of AI. This was purely for visualization purposes, and does not affect
# any implemented component of the project. This is the only file in the repository created using AI tools.
import pandas as pd

# Load dataset
df = pd.read_csv("pakistanHousingData.csv")

# Basic unique counts
print("Unique property IDs:", df["property_id"].nunique())
print("Unique cities:", df["city"].nunique())
print("Unique provinces:", df["province_name"].nunique())
print("Unique property types:", df["property_type"].nunique())
print("Unique bedroom counts:", df["bedrooms"].nunique())
print("Unique bathroom counts:", df["baths"].nunique())

# Unique value lists
print("\n--- Unique Cities ---")
print(df["city"].dropna().unique())

print("\n--- Unique Provinces ---")
print(df["province_name"].dropna().unique())

print("\n--- Unique Property Types ---")
print(df["property_type"].dropna().unique())

print("\n--- Unique Bedroom Counts ---")
print(df["bedrooms"].dropna().unique())

print("\n--- Unique Bathroom Counts ---")
print(df["baths"].dropna().unique())

# Frequency tables
print("\n--- Listings per City ---")
print(df["city"].value_counts())

print("\n--- Listings per Province ---")
print(df["province_name"].value_counts())

print("\n--- Listings per Property Type ---")
print(df["property_type"].value_counts())

print("\n--- Listings per Bedroom Count ---")
print(df["bedrooms"].value_counts())

print("\n--- Listings per Bathroom Count ---")
print(df["baths"].value_counts())


