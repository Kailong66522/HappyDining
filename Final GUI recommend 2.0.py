import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import tkintermapview
import pandas as pd
import random


excel_file_1 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhi.xlsx"
df1 = pd.read_excel(excel_file_1)
open_toplevels = []

def close_old_toplevels():
    for window in open_toplevels:
        window.destroy()
    open_toplevels.clear()

def show_info(restaurant):
    extra_window5 = ctk.CTkToplevel()
    open_toplevels.append(extra_window5)
    extra_window5.geometry('600x600')
    extra_window5.grab_set()  
    extra_window5.lift()
    extra_window5.attributes('-topmost', True)
    ctk.CTkLabel(extra_window5, text=restaurant).pack()
    extra_window5.wait_window()

def get_location(restaurant):
    def get_coord(val):
        s = str(int(val))
        return float(s[:2] + "." + s[2:])
    return (get_coord(restaurant["Latitude"]), get_coord(restaurant["Longitude"]))

def show_on_map(restaurant):
    window = ctk.CTkToplevel()
    window.geometry(f"{800}x{600}")
    window.title("Location")
    window.lift()
    window.attributes('-topmost',True)
    window.focus_force() 
    map_widget = tkintermapview.TkinterMapView(window, corner_radius=0, max_zoom=17)
    map_widget.pack(fill="both", expand=True)
    location = get_location(restaurant)
    marker = map_widget.set_position(*location, text=restaurant["Restaurant Name"], marker=True, command=lambda x: show_info(restaurant))




def best_rest():
    max_index = df1['Z-number'].idxmax()
    max_row = df1.loc[max_index]
    show_on_map(max_row)
    

def choice_rest():
    close_old_toplevels()
    choice_window = ctk.CTkToplevel()
    choice_window.geometry('400x300')
    choice_window.grab_set() 
    choice_window.lift()
    choice_window.attributes('-topmost', True)
    choice_window.title("User preferences")
    ctk.CTkLabel(choice_window, text= 'Please insert Preferences').pack() 

    choices = set()
    for entry in df1["Cuisines"]:
        choices.update([cuisine.strip() for cuisine in entry.split(",")])
    cuisine_choice = tk.StringVar()
    option_box = ctk.CTkOptionMenu(choice_window, variable=cuisine_choice, values=list(choices))
    option_box.pack()
    cuisine_choice.set("North Indian")

    ctk.CTkLabel(choice_window, text= 'How much Indian Rupees do you want to spend for two?').pack()
    rupee_entry = ctk.CTkEntry(choice_window)
    rupee_entry.insert(0, "1000")
    rupee_entry.pack()

    ctk.CTkLabel(choice_window, text= 'Whats the minimum amount of stars the restaurant should have?').pack()
    rating_entry = ctk.CTkEntry(choice_window)
    rating_entry.insert(0, "0")
    rating_entry.pack()

    delivery_check_var = ctk.BooleanVar(value=False)
    delivery_check = ctk.CTkCheckBox(choice_window, text= 'Should the restaurant be able to deliver your food?', variable=delivery_check_var)
    delivery_check.pack()

    book_check_var = ctk.BooleanVar(value=True)
    book_check = ctk.CTkCheckBox(choice_window, text= 'Should the restaurant have table booking?', variable=book_check_var)
    book_check.pack()

    remaining_var = ctk.StringVar()
    ctk.CTkLabel(choice_window, textvariable=remaining_var).pack()

    def filter_restaurants():
        cuisine =  cuisine_choice.get()
        cost = int(rupee_entry.get())
        rating = int(rating_entry.get())
        delivery = delivery_check_var.get()
        book = book_check_var.get()

        Cuisine = df1["Cuisines"].str.contains(cuisine)
        Cost = df1["Average Cost for two"] <= cost
        Rating = df1["Rating star"] >= rating
        Delivery = (df1["Has Online delivery"] == "Yes") == delivery
        Book = (df1["Has Table Booking"] == "Yes") == book

        filtered = df1[(Cuisine) & (Cost) & (Rating) & (Delivery) & (Book)]
        sorted_df = filtered.sort_values(by='Z-number', ascending=False)
        return sorted_df

    def update_remaining():
        remain = len(filter_restaurants())
        remaining_var.set(f"Restaurants Found: {remain}")

    rupee_entry.bind("<KeyRelease>", lambda x: update_remaining())
    rating_entry.bind("<KeyRelease>", lambda x: update_remaining())
    option_box.bind("<<ComboboxSelected>>", lambda x: update_remaining())
    delivery_check.bind("<Button-1>", lambda x: update_remaining())
    book_check.bind("<Button-1>", lambda x: update_remaining())

    def search():
        sorted_df = filter_restaurants()
        select_window = ctk.CTkToplevel()
        select_window.geometry('400x200')
        select_window.title("Best 3 Restaurants")
        ctk.CTkLabel(select_window, text= 'These are the 3 best restaurants based on your preferences').pack() 
        for i in range(min(3, len(sorted_df))):
            restaurant = sorted_df.iloc[i]
            a = ctk.CTkButton(select_window, text=restaurant["Restaurant Name"], command=lambda r=restaurant: show_on_map(r))
            a.pack(padx=5, pady=5)
    
        button4 = ctk.CTkButton(select_window, text='Close', command=select_window.destroy)
        button4.pack(padx=5, pady=5)
        
        if choice_window is not None:
            choice_window.destroy()




    button4 = ctk.CTkButton(choice_window, text='Enter', command = search)
    button4.pack()
  
def random_rest():
    num_rows = len(df1)
    random_index = random.randint(0, num_rows - 1)
    random_row = df1.iloc[random_index]
    show_on_map(random_row)


root = ctk.CTk()
root.title("Restaurant Recommendation System")  
root.geometry("800x400")
root.minsize(width=800 , height=400)

label1 = ctk.CTkLabel(root, text="Welcome to Kai's Dining Experience in New Delhi")
label1.pack(padx=20,pady=20)

label2 =ctk.CTkLabel(root, text="Please choose between the following:")
label2.pack(padx=5,pady=5)

button1 = ctk.CTkButton(root, text="1. Give me the best restaurant in the city",command=best_rest)
button1.pack(padx=5,pady=5)
button2 = ctk.CTkButton(root, text="2. Give me the best restaurant based on my preferences",command=choice_rest)
button2.pack(padx=5,pady=5)
button3 = ctk.CTkButton(root, text="3. Give me a random restaurant in my city",command=random_rest)
button3.pack(padx=5,pady=5)

quit_button = ctk.CTkButton(root, text="End Program", command=root.destroy)
quit_button.pack(padx=5,pady=5)

root.mainloop()