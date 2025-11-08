from dataset import Dataset

# This function creates a Dataset object out of the pieces of data selected in the dictionaries
def parseSelectedData(df, cityDict, propDict, bedDict, bathDict): # O(57n)

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

# This function is used to retrieve data from the backend to communicate with the frontend
def getSelectedData(df, cityDict, propDict, bedDict, bathDict): #O(57n)

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

    return df

