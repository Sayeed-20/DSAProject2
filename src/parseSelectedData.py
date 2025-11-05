import pandas as pd
from dataset import Dataset

# All False dictionaries:
cities = {"Islamabad": False,
            "Lahore": False,
            "Faisalabad": True,
            "Rawalpindi": False,
            "Karachi": True}
#
# propertyTypes = {"Flat": False,
#                  "House": False,
#                  "Penthouse": False,
#                  "Farm House": False,
#                  "Lower Portion": False,
#                  "Upper Portion": False}
#
# bedrooms = {"0": False,
#             "1": False,
#             "2": False,
#             "3": False,
#             "4": False,
#             "5": False,
#             "6": False,
#             "7": False,
#             "8": False,
#             "9": False,
#             "10": False,
#             "11": False,
#             "12": False,
#             "13": False,
#             "14": False,
#             "15": False,
#             "16": False,
#             "18": False,
#             "21": False,
#             "25": False,
#             "27": False,
#             "28": False,
#             "68": False}
#
bathrooms = {"0": True,
             "1": False,
             "2": False,
             "3": False,
             "4": False,
             "5": False,
             "6": False,
             "7": False,
             "8": False,
             "9": False,
             "10": False,
             "11": False,
             "12": False,
             "13": False,
             "14": False,
             "403": False}


# All true dictionaries:
# cities = {
#     "Islamabad": True,
#     "Lahore": True,
#     "Faisalabad": True,
#     "Rawalpindi": True,
#     "Karachi": True
# }

propertyTypes = {
    "Flat": True,
    "House": True,
    "Penthouse": True,
    "Farm House": True,
    "Lower Portion": True,
    "Upper Portion": True
}

bedrooms = {
    "0": True,
    "1": True,
    "2": True,
    "3": True,
    "4": True,
    "5": True,
    "6": True,
    "7": True,
    "8": True,
    "9": True,
    "10": True,
    "11": True,
    "12": True,
    "13": True,
    "14": True,
    "15": True,
    "16": True,
    "18": True,
    "21": True,
    "25": True,
    "27": True,
    "28": True,
    "68": True
}

# bathrooms = {
#     "0": True,
#     "1": True,
#     "2": True,
#     "3": True,
#     "4": True,
#     "5": True,
#     "6": True,
#     "7": True,
#     "8": True,
#     "9": True,
#     "10": True,
#     "11": True,
#     "12": True,
#     "13": True,
#     "14": True,
#     "403": True
# }


df = pd.read_csv("pakistanHousingData_cleaned.csv") # Not needed here, should be in main
df["bedrooms"] = df["bedrooms"].astype(str)
df["baths"] = df["baths"].astype(str)

def parseSelectedData(df, cityDict, propDict, bedDict, bathDict):


    for key in cityDict:
        if cityDict[key] == False:
            df = df[df["city"] != key]

    for key in propDict:
        if propDict[key] == False:
            df = df[df["property_type"] != key]

    for key in bedDict:
        if bedDict[key] == False:
            df = df[df["bedrooms"] != key]

    for key in bathDict:
        if bathDict[key] == False:
            df = df[df["baths"] != key]

    df = df.reset_index(drop=True)

    return Dataset(df)

# Testing:


selectedData = parseSelectedData(df, cities, propertyTypes, bedrooms, bathrooms)
for house in selectedData.data:
    print(house);