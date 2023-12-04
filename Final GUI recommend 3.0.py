import tkinter as tk
from tkinter import ttk     #Unnötig
from tkinter import messagebox  #Unnötig
import customtkinter as ctk
import tkintermapview
import pandas as pd
import random
from gower import gower_matrix
from sklearn.cluster import KMeans
import numpy as np


#Reading the Excel files and saving these in 2 dataframes
excel_file_2 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhiwahlgross.xlsx"
excel_file_1 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhi.xlsx"
df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)
open_toplevels = []

#Closing unnecessary windows
def close_old_toplevels():
    for window in open_toplevels:
        window.destroy()
    open_toplevels.clear()



#This function shows all the restaurant infos when clicking onto the pin in the map
def show_info(restaurant):
    extra_window5 = ctk.CTkToplevel()
    open_toplevels.append(extra_window5)
    extra_window5.geometry('600x600')
    extra_window5.grab_set()  
    extra_window5.lift()
    extra_window5.attributes('-topmost', True)
    ctk.CTkLabel(extra_window5, text=restaurant).pack()
    extra_window5.wait_window()

#shortly discussed in the seminar work, here the longitude and latitude get improved by adding a comma
def get_location(restaurant):
    def get_coord(val):
        s = str(int(val))
        return float(s[:2] + "." + s[2:])
    return (get_coord(restaurant["Latitude"]), get_coord(restaurant["Longitude"]))

#This functions allows the "openstreetmap" to open,and use the improved coordinates to show the restaurants location
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



#This functions shows the best restaurant in the whole list, the z-score plays a big role here, as also discussed in the work
def best_rest():
    max_index = df1['Z-number'].idxmax()
    max_row = df1.loc[max_index]
    show_on_map(max_row)
    

#Main function of the code, here the User can insert his preferences and create his "dream" restaurant that will be saved as a own vector in the excel table
def choice_rest():
    close_old_toplevels()
    choice_window = ctk.CTkToplevel()
    choice_window.geometry('400x650')
    choice_window.grab_set() 
    choice_window.lift()
    choice_window.attributes('-topmost', True)
    choice_window.title("User preferences")
    ctk.CTkLabel(choice_window, text= 'Please insert preferences').pack() 

    choices = set()
    #These functions explain themselves most of the time, the User can read the text of the question and then insert the right things according to the question
    #Here an OptionMenu "ctk.CTkOptionMenu" was chosen. A drop-down menu where the user can choose between all cities from the list
    ctk.CTkLabel(choice_window, text= 'Select the City the restaurant should be in').pack()
    #This for-loop searches for all the cities in the list and saves them as "choices"
    for entry in df1["City"]:
        choices.update([city.strip() for city in entry.split(",")])
    city_choice = tk.StringVar()
    #Here the contents of the option box/the drop-down menu get set to "choices".
    option_box = ctk.CTkOptionMenu(choice_window, variable=city_choice, values=list(choices))
    option_box.pack()
    #The standard value here in the optionbox is set to "New Delhi". If the User doesnt care in which city the restaurant is, he can just ignore this button
    city_choice.set("New Delhi")

    #Basically the same as above, a drop down menu with the verbose locality (example: Würzburg Innenstadt, Mainfrankentheater ,...)
    ctk.CTkLabel(choice_window, text= 'Select the Locality the restaurant should be at').pack()
    for entry in df1["Locality"]:
        choices.update([locality.strip() for locality in entry.split(",")])
    locality_choice = tk.StringVar()
    option_box = ctk.CTkOptionMenu(choice_window, variable=locality_choice, values=list(choices))
    option_box.pack()
    #Here the standard value is left clear, since not every verbose locality can fir to every city
    locality_choice.set(" ")

    #Here the for loop didnt work. Thats why the custom_value of the cuisines was manually typed. 
    custom_value = ["Afghani" ,"American","Armenian","Asian","Assamese","Awadhi","Bakery","Beverages","Biryani","Burger"
    "Burmese" ,"Cafe","Charcoal Grill","Chettinad","Chinese","Continental Cuisine","Cuisine Varies","Deli","Dessert"
    "Drinks Only","European","Fast Food","Finger Food","French", "Goan" ,"Greek", "Gujarati", "Healthy Food" ,"Hyderabadi" ,"Ice Cream" ,"Indonesian"
    "Iranian" ,"Italian", "Japanese", "Juices","Kerala", "Korean" ,"Lebanese", "Lucknowi" ,"Maharashtrian" ,"Malaysian", "Mediterranean" ,"Mexican"
    "Middle Eastern", "Mithai" ,"Modern", "Indian", "Mughlai","Naga" ,"Nepalese", "North Eastern" ,"North Indian", "Oriya", "Pakistani", "Parsi"
    "Pizza" ,"Portugese" ,"Rajasthani" ,"Raw Meats" ,"Salad" ,"Seafood", "South Indian", "Spanish", "Steak" ,"Street Food" ,"Sushi" ,"Tea" ,"Tex-Mex" ,"Thai" ,"Tibetan" ,"Turkish"]
    ctk.CTkLabel(choice_window, text= 'What Cuisine should the restaurant offer').pack()
    cuisine_choice = tk.StringVar()
    option_box = ctk.CTkOptionMenu(choice_window, variable=cuisine_choice, values=custom_value)
    option_box.pack()
    cuisine_choice.set("North Indian")
    
    #Here a ctk.CTkEntry menu was chosen, a small window where something can be entered.
    ctk.CTkLabel(choice_window, text= 'How much Indian Rupees do you want to spend for two?').pack()
    ctk.CTkLabel(choice_window, text= '100 Rupees = 1.10€ , 500 Rupees = 5.50€, 1000 Rupees = 10.99€').pack()
    rupee_entry = ctk.CTkEntry(choice_window)
    #Standardvalue is set to 1000 rupees
    rupee_entry.insert(0, "1000")
    rupee_entry.pack()

    ctk.CTkLabel(choice_window, text= 'How much stars should the restaurant have?').pack()
    rating_entry = ctk.CTkEntry(choice_window)
    rating_entry.insert(0, "0")
    rating_entry.pack()


    #Drop-down menus with the possibility to enter only "Yes" or "No", with the standardvalue being "No"
    custom_values = ["Yes", "No"]
    ctk.CTkLabel(choice_window, text= 'Should the Restaurant be able to deliver your food?').pack()
    delivery_choice = tk.StringVar()
    option_box = ctk.CTkOptionMenu(choice_window, variable=delivery_choice, values=custom_values)
    option_box.pack()
    delivery_choice.set("No")

    ctk.CTkLabel(choice_window, text= 'Should the Restaurant have Table booking?').pack()
    booking_choice = tk.StringVar()
    option_box = ctk.CTkOptionMenu(choice_window, variable=booking_choice, values=custom_values)
    option_box.pack()
    booking_choice.set("No")

    ctk.CTkLabel(choice_window, text= 'Whats the minimum amount of votes the restaurant should have?').pack()
    votes_entry = ctk.CTkEntry(choice_window)
    votes_entry.insert(0, "0")
    votes_entry.pack(padx=5, pady=8)


    def search():
        #Here all the inputs from the User get inserted to each variable
        selected_vector = pd.DataFrame({
        'City': [city_choice.get()],
        'Locality Verbose': [locality_choice.get()],
        'Cuisines': [cuisine_choice.get()],
        'Average Cost for two': [int(rupee_entry.get())],
        'Has Table Booking': [booking_choice.get()],
        'Has Online delivery': [delivery_choice.get()],
        'Rating star': [int(rating_entry.get())],
        'Votes': [int(votes_entry.get())]

    })
        #A simple T-kinter window
        select_window = ctk.CTkToplevel()
        select_window.geometry('400x200')
        select_window.title("Best Restaurants")
        ctk.CTkLabel(select_window, text= 'These are the 3 best restaurants based on your preferences').pack() 

        # Here the relevant columns for the calculation of the Gower distance get selected (This is the whole new dataframe (df2) that was created for this use)
        selected_columns = ['City', 'Locality Verbose','Cuisines', 'Average Cost for two', 'Has Table Booking', 'Has Online delivery',
                            'Rating star', 'Votes']
        
        #Calculation of the Gower distance for all Vectors with the selected columns
        gower_dist_matrix = gower_matrix(df2[selected_columns], df2[selected_columns])

        #K is the number of clusters that have been identified with the "Elbow" method
        k = 2 

        #The function that uses K-means clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        clusters = kmeans.fit_predict(gower_dist_matrix)

        #Here the ckuster-index of the new "dream" restaurant is found
        selected_vector_cluster = kmeans.predict(gower_matrix(selected_vector[selected_columns], df2[selected_columns]))[0]

        #Here the Indices of the same vektors in the cluster get searched
        same_cluster_indices = np.where(clusters == selected_vector_cluster)[0]

        #Printing the whole cluster in the console, listing all the restaurants
        print("Vectors in the same cluster as the selected vector:")
        print(df2.iloc[same_cluster_indices])

        #Creating the Gower distance matrix between the "dream" restaurant and all the other vectors in the cluster
        gower_distances_same_cluster = gower_matrix(selected_vector[selected_columns], df2.iloc[same_cluster_indices][selected_columns])
        print(gower_distances_same_cluster)

        #Here the closest vector is searched and printed in the console
        nearest_vector_index_in_cluster = np.argmin(gower_distances_same_cluster)
        print("Index in the cluster:", nearest_vector_index_in_cluster)

        #Here the Index of the found vecotrs gets searched in the actual Excel file (df1) to print the right restaurant
        nearest_vector_index_in_original = same_cluster_indices[nearest_vector_index_in_cluster]
        print("Index in the original DataFrame (df1):", nearest_vector_index_in_original)

        #printing the nearest vector in the console
        print("Nearest Vector within the same cluster:")
        print(df1.iloc[nearest_vector_index_in_original])

        #Here the 3 nearest vectors are found with the help of the Gower distance
        nearest_vector_indices_in_original = same_cluster_indices[np.argsort(gower_distances_same_cluster.flatten())[:3]]

        #Here the 3 nearest vectors get shown as buttons with the restaurant name in a tkinter window
        for idx in nearest_vector_indices_in_original:
            restaurant = df1.iloc[idx]
            a = ctk.CTkButton(select_window, text=restaurant["Restaurant Name"], command=lambda r=restaurant: show_on_map(r))
            a.pack(padx=5, pady=5)


        # Closing the window with the close button
        button4 = ctk.CTkButton(select_window, text='Close', command=select_window.destroy)
        button4.pack(padx=5, pady=5)
        #Fenster is closed if its still on the scree, this function tries to solve an issue because the unnecessary windows should close after usage
        if choice_window is not None:
            choice_window.destroy()




    button4 = ctk.CTkButton(choice_window, text='Enter', command = search)
    button4.pack()

#The function for the random restaurant, here the library "random" is used to get a random index of the Excel table
def random_rest():
    num_rows = len(df1)
    random_index = random.randint(0, num_rows - 1)
    random_row = df1.iloc[random_index]
    show_on_map(random_row)

#This is the main window with all the buttons from CustomTkinter, with a click on each button the matching command is executed
root = ctk.CTk()
root.title("Restaurant Recommendation System")  
root.geometry("800x400")
root.minsize(width=800 , height=400)

label1 = ctk.CTkLabel(root, text="Welcome to Kai's Dining Experience in New Delhi")
label1.pack(padx=20,pady=20)

label2 =ctk.CTkLabel(root, text="Please choose between the following:")
label2.pack(padx=5,pady=5)

button1 = ctk.CTkButton(root, text="1. Give me the best restaurant in the city",command=best_rest)  #best restaurant
button1.pack(padx=5,pady=5)
button2 = ctk.CTkButton(root, text="2. Give me the best 3 restaurants based on my preferences",command=choice_rest) #restaurant based on preferences
button2.pack(padx=5,pady=5)
button3 = ctk.CTkButton(root, text="3. Give me a random restaurant in my city",command=random_rest) #random restaurant 
button3.pack(padx=5,pady=5)

#End program with "destroy"
quit_button = ctk.CTkButton(root, text="End Program", command=root.destroy)
quit_button.pack(padx=5,pady=5)

#Mainloop to keep all the windows open

root.mainloop()