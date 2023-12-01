import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import random

excel_file_1 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhi.xlsx"
df1 = pd.read_excel(excel_file_1)


def best_rest():
    extra_window = tk.Toplevel()
    extra_window.geometry("350x450")
    ttk.Label(extra_window, text= 'The best restaurant in the city is: ').pack()
    max_index = df1['Z-number'].idxmax()
    # Extract the entire row associated with the maximum value
    max_row = df1.loc[max_index]
    ttk.Label(extra_window, text= max_row).pack()
def choice_rest():
    extra_window = tk.Toplevel()
    extra_window.geometry('300x150')
    ttk.Label(extra_window, text= 'What cuisine should the Restaurant have?').pack() 
    entry1 = ttk.Entry(extra_window)
    entry1.pack()
    def cuisine():
        cuisine = entry1.get()
        Cuisine2 = df1['Cuisines'] == cuisine
        extra_window2 = tk.Toplevel()
        extra_window.geometry('300x150')
        ttk.Label(extra_window2, text= 'How much Indian Rupees do you want to spend for two?').pack()
        entry2 = ttk.Entry(extra_window2)
        entry2.pack()
        def rupee():
            rupees_str = entry2.get()
            try:
                rupees = int(rupees_str)
                Rupees2 = df1['Average Cost for two'] <= rupees
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer for the budget.")
                root.destroy()
            extra_window3 = tk.Toplevel()
            extra_window3.geometry('300x200')
            ttk.Label(extra_window3, text= 'How many Stars should the Restaurant have?').pack()
            def rating1():
                Rating = df1['Rating star'] == 5
                extra_window4 = tk.Toplevel()
                extra_window4.geometry('350x200')
                ttk.Label(extra_window4, text= 'Do you wish to have the food delivered or go to the restaurant?').pack()
                def delivered():
                    Booking = df1['Has Table Booking'] == 'Yes'
                    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking)]
                    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                    if len(sorted_df) >= 3:
                        first_three_rows = sorted_df.head(3)
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                        first_three_rows = sorted_df
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                def restaurant():
                    Deliver = df1['Has Online delivery'] == 'No'
                    msg_box = tk.messagebox.askyesno('Table Booking', 'Do you wish to Book a Table for your visit?')
                    if msg_box == 'yes':
                        Booking = df1['Has Table Booking'] == 'Yes'
                        filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                        sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                        if len(sorted_df) >= 3:
                            first_three_rows = sorted_df.head(3)
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                        else:
                            first_three_rows = sorted_df
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                            Booking = df1['Has Table Booking'] == 'No'
                            filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                            sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                            if len(sorted_df) >= 3:
                                first_three_rows = sorted_df.head(3)
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                            else:
                                first_three_rows = sorted_df
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                button12 = ttk.Button(extra_window4, text= 'Delivered', command = delivered)
                button12.pack()
                button13 = ttk.Button(extra_window4, text= 'Go to Restaurant', command = restaurant)
                button13.pack()
            def rating2():
                Rating = df1['Rating star'] >= 4
                extra_window4 = tk.Toplevel()
                extra_window4.geometry('350x200')
                ttk.Label(extra_window4, text= 'Do you wish to have the food delivered or go to the restaurant?').pack()
                def delivered():
                    Booking = df1['Has Table Booking'] == 'Yes'
                    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking)]
                    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                    if len(sorted_df) >= 3:
                        first_three_rows = sorted_df.head(3)
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                        first_three_rows = sorted_df
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                def restaurant():
                    Deliver = df1['Has Online delivery'] == 'No'
                    msg_box = tk.messagebox.askyesno('Table Booking', 'Do you wish to Book a Table for your visit?')
                    if msg_box == 'yes':
                        Booking = df1['Has Table Booking'] == 'Yes'
                        filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                        sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                        if len(sorted_df) >= 3:
                            first_three_rows = sorted_df.head(3)
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                        else:
                            first_three_rows = sorted_df
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                            Booking = df1['Has Table Booking'] == 'No'
                            filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                            sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                            if len(sorted_df) >= 3:
                                first_three_rows = sorted_df.head(3)
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                            else:
                                first_three_rows = sorted_df
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                button12 = ttk.Button(extra_window4, text= 'Delivered', command = delivered)
                button12.pack()
                button13 = ttk.Button(extra_window4, text= 'Go to Restaurant', command = restaurant)
                button13.pack()
            def rating3():
                Rating = df1['Rating star'] >= 3
                extra_window4 = tk.Toplevel()
                extra_window4.geometry('350x200')
                ttk.Label(extra_window4, text= 'Do you wish to have the food delivered or go to the restaurant?').pack()
                def delivered():
                    Booking = df1['Has Table Booking'] == 'Yes'
                    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking)]
                    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                    if len(sorted_df) >= 3:
                        first_three_rows = sorted_df.head(3)
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                        first_three_rows = sorted_df
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                def restaurant():
                    Deliver = df1['Has Online delivery'] == 'No'
                    msg_box = tk.messagebox.askyesno('Table Booking', 'Do you wish to Book a Table for your visit?')
                    if msg_box == 'yes':
                        Booking = df1['Has Table Booking'] == 'Yes'
                        filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                        sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                        if len(sorted_df) >= 3:
                            first_three_rows = sorted_df.head(3)
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                        else:
                            first_three_rows = sorted_df
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                            Booking = df1['Has Table Booking'] == 'No'
                            filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                            sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                            if len(sorted_df) >= 3:
                                first_three_rows = sorted_df.head(3)
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                            else:
                                first_three_rows = sorted_df
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                button12 = ttk.Button(extra_window4, text= 'Delivered', command = delivered)
                button12.pack()
                button13 = ttk.Button(extra_window4, text= 'Go to Restaurant', command = restaurant)
                button13.pack()
            def rating4():
                Rating = df1['Rating star'] >= 2
                extra_window4 = tk.Toplevel()
                extra_window4.geometry('350x200')
                ttk.Label(extra_window4, text= 'Do you wish to have the food delivered or go to the restaurant?').pack()
                def delivered():
                    Booking = df1['Has Table Booking'] == 'Yes'
                    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking)]
                    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                    if len(sorted_df) >= 3:
                        first_three_rows = sorted_df.head(3)
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                        first_three_rows = sorted_df
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                def restaurant():
                    Deliver = df1['Has Online delivery'] == 'No'
                    msg_box = tk.messagebox.askyesno('Table Booking', 'Do you wish to Book a Table for your visit?')
                    if msg_box == 'yes':
                        Booking = df1['Has Table Booking'] == 'Yes'
                        filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                        sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                        if len(sorted_df) >= 3:
                            first_three_rows = sorted_df.head(3)
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                        else:
                            first_three_rows = sorted_df
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                            Booking = df1['Has Table Booking'] == 'No'
                            filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                            sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                            if len(sorted_df) >= 3:
                                first_three_rows = sorted_df.head(3)
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                            else:
                                first_three_rows = sorted_df
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                button12 = ttk.Button(extra_window4, text= 'Delivered', command = delivered)
                button12.pack()
                button13 = ttk.Button(extra_window4, text= 'Go to Restaurant', command = restaurant)
                button13.pack()
            def rating5():
                Rating = df1['Rating star'] >= 1
                extra_window4 = tk.Toplevel()
                extra_window4.geometry('350x200')
                ttk.Label(extra_window4, text= 'Do you wish to have the food delivered or go to the restaurant?').pack()
                def delivered():
                    Booking = df1['Has Table Booking'] == 'Yes'
                    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking)]
                    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                    if len(sorted_df) >= 3:
                        first_three_rows = sorted_df.head(3)
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                        first_three_rows = sorted_df
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                def restaurant():
                    Deliver = df1['Has Online delivery'] == 'No'
                    msg_box = tk.messagebox.askyesno('Table Booking', 'Do you wish to Book a Table for your visit?')
                    if msg_box == 'yes':
                        Booking = df1['Has Table Booking'] == 'Yes'
                        filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                        sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                        if len(sorted_df) >= 3:
                            first_three_rows = sorted_df.head(3)
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                        else:
                            first_three_rows = sorted_df
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                            Booking = df1['Has Table Booking'] == 'No'
                            filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                            sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                            if len(sorted_df) >= 3:
                                first_three_rows = sorted_df.head(3)
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                            else:
                                first_three_rows = sorted_df
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                button12 = ttk.Button(extra_window4, text= 'Delivered', command = delivered)
                button12.pack()
                button13 = ttk.Button(extra_window4, text= 'Go to Restaurant', command = restaurant)
                button13.pack()
            def rating6():
                Rating = df1['Rating star'] >= 0
                extra_window4 = tk.Toplevel()
                extra_window4.geometry('350x200')
                ttk.Label(extra_window4, text= 'Do you wish to have the food delivered or go to the restaurant?').pack()
                def delivered():
                    Booking = df1['Has Table Booking'] == 'Yes'
                    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking)]
                    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                    if len(sorted_df) >= 3:
                        first_three_rows = sorted_df.head(3)
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                        first_three_rows = sorted_df
                        extra_window5 = tk.Toplevel()
                        extra_window5.geometry('1200x200')
                        ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                        ttk.Label(extra_window5, text= first_three_rows).pack()
                def restaurant():
                    Deliver = df1['Has Online delivery'] == 'No'
                    msg_box = tk.messagebox.askyesno('Table Booking', 'Do you wish to Book a Table for your visit?')
                    if msg_box == 'yes':
                        Booking = df1['Has Table Booking'] == 'Yes'
                        filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                        sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                        if len(sorted_df) >= 3:
                            first_three_rows = sorted_df.head(3)
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                        else:
                            first_three_rows = sorted_df
                            extra_window5 = tk.Toplevel()
                            extra_window5.geometry('1200x200')
                            ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                            ttk.Label(extra_window5, text= first_three_rows).pack()
                    else:
                            Booking = df1['Has Table Booking'] == 'No'
                            filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
                            sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
                            if len(sorted_df) >= 3:
                                first_three_rows = sorted_df.head(3)
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                            else:
                                first_three_rows = sorted_df
                                extra_window5 = tk.Toplevel()
                                extra_window5.geometry('1200x200')
                                ttk.Label(extra_window5, text= "Here are the 3 best Restaurants based on your preferences").pack()
                                ttk.Label(extra_window5, text= first_three_rows).pack()
                button12 = ttk.Button(extra_window4, text= 'Delivered', command = delivered)
                button12.pack()
                button13 = ttk.Button(extra_window4, text= 'Go to Restaurant', command = restaurant)
                button13.pack()
            button6 = ttk.Button(extra_window3, text= '5 stars', command = rating1)
            button6.pack()
            button7 = ttk.Button(extra_window3, text= '4 or more stars', command = rating2)
            button7.pack()
            button8 = ttk.Button(extra_window3, text= '3 or more stars', command = rating3)
            button8.pack()
            button9 = ttk.Button(extra_window3, text= '2 or more stars', command = rating4)
            button9.pack()
            button10 = ttk.Button(extra_window3, text= '1 or more stars', command = rating5)
            button10.pack()
            button11 = ttk.Button(extra_window3, text= 'It can be a new not rated Restaurant', command = rating6)
            button11.pack()
        button5 = ttk.Button(extra_window2, text= 'Enter', command = rupee)
        button5.pack()
    button4 = ttk.Button(extra_window, text='Enter', command = cuisine)
    button4.pack()
    def extra():
        extra_windowx = tk.Toplevel()
        extra_windowx.geometry('600x250')
        ttk.Label(extra_windowx, text= 'Afghani, American, Armenian, Asian, Assamese, Awadhi, Bakery, Beverages').pack()
        ttk.Label(extra_windowx, text= 'Biryani, Burger, Burmese, Cafe, Charcoal Grill, Chettinad, Chinese, Continental').pack()
        ttk.Label(extra_windowx, text= 'Cuisine, Cuisine Varies, Deli, Dessert, Drinks Only, European, Fast Food').pack()
        ttk.Label(extra_windowx, text= 'Finger Food, French, Goan, Greek, Gujarati, Healthy Food, Hyderabadi, Ice Cream').pack()
        ttk.Label(extra_windowx, text= 'Indonesian, Iranian, Italian, Japanese, Juices, Kerala, Korean, Lebanese, Lucknowi').pack()
        ttk.Label(extra_windowx, text= 'Maharashtrian, Malaysian, Mediterranean, Mexican, Middle Eastern, Mithai, Modern Indian').pack()
        ttk.Label(extra_windowx, text= 'Mughlai, Naga, Nepalese, North Eastern, North Indian, Oriya, Pakistani, Parsi, Pizza, Portugese').pack()
        ttk.Label(extra_windowx, text= 'Rajasthani, Raw Meats, Salad, Seafood, South Indian, Spanish, Steak, Street Food').pack()
        ttk.Label(extra_windowx, text= 'Sushi, Tea, Tex-Mex, Thai, Tibetan, Turkish').pack()
    buttonx = ttk.Button(extra_window, text = '--> For a list of all cuisines click here <--', command= extra)
    buttonx.pack()
def random_rest():
    extra_window = tk.Toplevel()
    extra_window.geometry('350x450')
    ttk.Label(extra_window, text= 'Heres a random restaurant in your city: ').pack()
    num_rows = len(df1)
    random_index = random.randint(0, num_rows - 1)
    random_row = df1.iloc[random_index]
    ttk.Label(extra_window, text= random_row).pack()
def ask_yes_no():
    answer = messagebox.askquestion('Title' , 'body')



root = tk.Tk()
root.title("Restaurant Recommendation System")  
root.geometry("800x400")
root.minsize(width=800 , height=400)

label1 = tk.Label(root, text="Welcome to Kai's Dining Experience in New Delhi" , bg="lightblue")
label1.pack()

label2 =tk.Label(root, text="Please choose between the following:" , bg="lightblue")
label2.pack()

button1 = ttk.Button(root, text="1. Give me the best restaurant in the city", padding=20,command=best_rest)
button1.pack()
button2 = ttk.Button(root, text="2. Give me the best restaurant thats specialized in a certain cuisine", padding=20,command=choice_rest)
button2.pack()
button3 = ttk.Button(root, text="3. Give me a random restaurant in my city", padding=20,command=random_rest)
button3.pack()

quit_button = ttk.Button(root, text="End Program",padding=20 , command=root.destroy)
quit_button.pack()
root.mainloop()