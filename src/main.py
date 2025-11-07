import pandas as pd
import tkinter as tk
import parseSelectedData


# Read dataset
df = pd.read_csv("pakistanHousingData_cleaned.csv") # Not needed here, should be in main
df["bedrooms"] = df["bedrooms"].astype(str)
df["baths"] = df["baths"].astype(str)

# Selection dictionaries (start with all unselected)
selectedCities = {"Islamabad": False,
            "Lahore": False,
            "Faisalabad": False,
            "Rawalpindi": False,
            "Karachi": False}

selectedPropTypes = {"Flat": False,
                 "House": False,
                 "Penthouse": False,
                 "Farm House": False,
                 "Lower Portion": False,
                 "Upper Portion": False}

selectedBedrooms = {"0": False,
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
            "15": False,
            "16": False,
            "18": False,
            "21": False,
            "25": False,
            "27": False,
            "28": False,
            "68": False}

selectedBathrooms = {"0": False,
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



# ----- Front End -----



# Initialize Window
window = tk.Tk()
window.title("Pakistani Property Sorter")
window.geometry("800x400")



# City selection
cityLabel = tk.Label(window, text="Cities")
cityLabel.place(x=550, y=30)

cityBox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=4)
for key in selectedCities:
    cityBox.insert(tk.END, key)

def toggleCityDropdown():
    if cityBox.winfo_viewable():
        cityBox.place_forget()
    else:
        cityBox.place(x=550, y=80)
        cityBox.lift()

def updateSelectedCities(event):
    selected = [cityBox.get(i) for i in cityBox.curselection()]
    for key in selectedCities:
        if key in selected:
            selectedCities[key] = True
        else:
            selectedCities[key] = False
        print("key: ", key, "val: ", selectedCities[key])

cityBox.bind("<<ListboxSelect>>", updateSelectedCities)
cityDropdown = tk.Button(window, text="Select Cities:", command=toggleCityDropdown)
cityDropdown.place(x=550, y=50)



# Property Type selection
propTypeLabel = tk.Label(window, text="Property Types")
propTypeLabel.place(x=550, y=110)

propTypeBox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=4)
for key in selectedPropTypes:
    propTypeBox.insert(tk.END, key)

def togglePropTypeDropdown():
    if propTypeBox.winfo_viewable():
        propTypeBox.place_forget()
    else:
        propTypeBox.place(x=550, y=160)
        propTypeBox.lift()

def updateSelectedPropTypes(event):
    selected = [propTypeBox.get(i) for i in propTypeBox.curselection()]
    for key in selectedPropTypes:
        if key in selected:
            selectedPropTypes[key] = True
        else:
            selectedPropTypes[key] = False
        print("key: ", key, "val: ", selectedPropTypes[key])

propTypeBox.bind("<<ListboxSelect>>", updateSelectedPropTypes)
propTypeDropdown = tk.Button(window, text="Select Property Types:", command=togglePropTypeDropdown)
propTypeDropdown.place(x=550, y=130)

window.mainloop()







