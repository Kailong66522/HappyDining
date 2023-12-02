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


#Einlesen der Excel-Tabellen mit Pandas
excel_file_2 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhiwahlgross.xlsx"
excel_file_1 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhi.xlsx"
df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)
open_toplevels = []

#Hier sollen unnötige Fenster geschlossen werden
def close_old_toplevels():
    for window in open_toplevels:
        window.destroy()
    open_toplevels.clear()



#Das ist die Funktion die die Daten anzeigt wenn man auf den Pin auf der Karte klickt
def show_info(restaurant):
    extra_window5 = ctk.CTkToplevel()
    open_toplevels.append(extra_window5)
    extra_window5.geometry('600x600')
    extra_window5.grab_set()  
    extra_window5.lift()
    extra_window5.attributes('-topmost', True)
    ctk.CTkLabel(extra_window5, text=restaurant).pack()
    extra_window5.wait_window()

#Kurz in der Seminararbeit darauf eingegangen, hier werden Longitude und Latitude mit kommas verbessert
def get_location(restaurant):
    def get_coord(val):
        s = str(int(val))
        return float(s[:2] + "." + s[2:])
    return (get_coord(restaurant["Latitude"]), get_coord(restaurant["Longitude"]))

#Diese funktion ist dafür da, dass beim Klicken auf den restaurantnamen und bei random/best restaurant eine OpenstreeMap-karte geöffnet wird
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



#Das ist die Funktion die das "Beste Restaurant" ausgibt, hier spielt die Z-nummer eine große Rolle, da somit das authentischste Restaurant gefunden werden kann
def best_rest():
    max_index = df1['Z-number'].idxmax()
    max_row = df1.loc[max_index]
    show_on_map(max_row)
    
#Die hauptfunktion in meinem Code, hier kann der User seine Präferenzen angeben.
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
    #Hier sind die funktionen alle relativ selbsterklärend am text. Der User liest die frage und kann dort dann seine sachen eingeben. 
    #Hier ist das ein OptionMenu wie es bei ctk.CTkOptionMenu steht, also ein drop-down menu bei dem er zwischen den Städten auswählen kann
    ctk.CTkLabel(choice_window, text= 'Select the City the restaurant should be in').pack()
    #Diese for-Schleife sucht quasi alle in der Excel tabelle enthaltenen Städte raus und speichert sie als "choices"
    for entry in df1["City"]:
        choices.update([city.strip() for city in entry.split(",")])
    city_choice = tk.StringVar()
    #Hier wird der Inhalt der option box also dem Drop-down menu = "choices" gesetzt. Also alle städte
    option_box = ctk.CTkOptionMenu(choice_window, variable=city_choice, values=list(choices))
    option_box.pack()
    #Der standartwert in dem optionbox menu ist "New Delhi", hier kann der User einfach nichts machen und es wird standartmäßig "New Delhi angegeben"
    city_choice.set("New Delhi")

    #Quasi das gleiche hier wieder, ein drop down menu, diesmal mit der Lokalität, also dem Ort (Wie z.B.: Würzburg Innenstadt, Mainfrankentheater usw.)
    ctk.CTkLabel(choice_window, text= 'Select the Locality the restaurant should be at').pack()
    for entry in df1["Locality"]:
        choices.update([locality.strip() for locality in entry.split(",")])
    locality_choice = tk.StringVar()
    option_box = ctk.CTkOptionMenu(choice_window, variable=locality_choice, values=list(choices))
    option_box.pack()
    #hier wird der Standartwert einfach leer gelassen, weil nicht jede Lokalität zu jeder Stadt passt 
    locality_choice.set(" ")

    #Hier hat meine for-Schleife für die Küchen irgendwie nicht funktioniert, deswegen habe ich die value manuell eingegeben...
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
    
    
    #hier ist jetzt ein cttk.CTkEntry menu, also ein kleines Fenster indem man was eingeben kann
    ctk.CTkLabel(choice_window, text= 'How much Indian Rupees do you want to spend for two?').pack()
    ctk.CTkLabel(choice_window, text= '100 Rupees = 1.10€ , 500 Rupees = 5.50€, 1000 Rupees = 10.99€').pack()
    rupee_entry = ctk.CTkEntry(choice_window)
    #Standartwert wurde hier auf 1000 Rupees gesetzt
    rupee_entry.insert(0, "1000")
    rupee_entry.pack()

    ctk.CTkLabel(choice_window, text= 'How much stars should the restaurant have?').pack()
    rating_entry = ctk.CTkEntry(choice_window)
    rating_entry.insert(0, "0")
    rating_entry.pack()


    #Drop-down Menus mit der möglichkeit Ja und Nein, und standartmäßig ist hier Nein angegeben
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
        #hier werden alle eingaben vom User eingesetzt
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
        #Ein Tkinter Fenster
        select_window = ctk.CTkToplevel()
        select_window.geometry('400x200')
        select_window.title("Best Restaurants")
        ctk.CTkLabel(select_window, text= 'These are the 3 best restaurants based on your preferences').pack() 

        # Hier werden die wichtigen und relevanten Spalten der Gower distanz berechnung angegeben (Quasi die ganze Excel Tabelle die extra dafür erstellt wurde)
        selected_columns = ['City', 'Locality Verbose','Cuisines', 'Average Cost for two', 'Has Table Booking', 'Has Online delivery',
                            'Rating star', 'Votes']
        
        #Berechnen der Gower distanz matrix für alle Vectoren mit den ausgewählten spalten 
        gower_dist_matrix = gower_matrix(df2[selected_columns], df2[selected_columns])

        # K ist die nummer der Cluster, die mithilfe der Elbow methode auf 2 gesetzt wurden
        k = 2 

        #Das ist die funktion die K-means clustering durchführt
        kmeans = KMeans(n_clusters=k, random_state=42)
        clusters = kmeans.fit_predict(gower_dist_matrix)

        #Hier wird der cluster-index des "traum restaurants" gefunden
        selected_vector_cluster = kmeans.predict(gower_matrix(selected_vector[selected_columns], df2[selected_columns]))[0]

        #Hier werden die Indexe der selben vektoren im cluster und dem traum restaurant gesucht 
        same_cluster_indices = np.where(clusters == selected_vector_cluster)[0]

        # Hier wird quasi das ganze cluster geprintet und alle restaurants aufgelistet 
        print("Vectors in the same cluster as the selected vector:")
        print(df2.iloc[same_cluster_indices])

        #Hier wird die gower distanz matrix erstellt zwischen dem "Traum restaurant" und den anderen Vektoren in dem cluster 
        gower_distances_same_cluster = gower_matrix(selected_vector[selected_columns], df2.iloc[same_cluster_indices][selected_columns])
        print(gower_distances_same_cluster)
        #Hier wird der näheste vector gesucht und der Index in der Konsole ausgegeben 
        nearest_vector_index_in_cluster = np.argmin(gower_distances_same_cluster)
        print("Index in the cluster:", nearest_vector_index_in_cluster)

        #hier wird der Index der Vektoren gesucht, da aktuell nur der index in dem anderen Dataframe (Excel Tabelle) bekannt ist
        nearest_vector_index_in_original = same_cluster_indices[nearest_vector_index_in_cluster]
        print("Index in the original DataFrame (df1):", nearest_vector_index_in_original)

        # printen des nähesten vectors in der Konsole
        print("Nearest Vector within the same cluster:")
        print(df1.iloc[nearest_vector_index_in_original])

        #Hier werden die 3 nähesten vectoren gesucht mithilfer der gower distanz
        nearest_vector_indices_in_original = same_cluster_indices[np.argsort(gower_distances_same_cluster.flatten())[:3]]

        #Hier werden die 3. nähesten vectoren als buttons ausgegeben 
        for idx in nearest_vector_indices_in_original:
            restaurant = df1.iloc[idx]
            a = ctk.CTkButton(select_window, text=restaurant["Restaurant Name"], command=lambda r=restaurant: show_on_map(r))
            a.pack(padx=5, pady=5)


        # Fenster schliessen mit dem Close buton 
        button4 = ctk.CTkButton(select_window, text='Close', command=select_window.destroy)
        button4.pack(padx=5, pady=5)
        #Fenster wird geschlossen wenn es noch da ist, diese fkt ist ein versuch für eine Fehlerbehebung, da ich wollte, dass manche Fenster nach dem ausführen geschlossen werden
        if choice_window is not None:
            choice_window.destroy()




    button4 = ctk.CTkButton(choice_window, text='Enter', command = search)
    button4.pack()


#Die fkt für das Zufällige restaurant nimmt mit random einen zufälligen index aus der Excel Tabelle.
def random_rest():
    num_rows = len(df1)
    random_index = random.randint(0, num_rows - 1)
    random_row = df1.iloc[random_index]
    show_on_map(random_row)

#Das ist das Hauptfenster mit allen Buttons aus CustomTkinter, mit dem click auf den Button wird die zugehörige command fkt ausgeführt
root = ctk.CTk()
root.title("Restaurant Recommendation System")  
root.geometry("800x400")
root.minsize(width=800 , height=400)

label1 = ctk.CTkLabel(root, text="Welcome to Kai's Dining Experience in New Delhi")
label1.pack(padx=20,pady=20)

label2 =ctk.CTkLabel(root, text="Please choose between the following:")
label2.pack(padx=5,pady=5)

button1 = ctk.CTkButton(root, text="1. Give me the best restaurant in the city",command=best_rest)  #bestes restaurant fkt
button1.pack(padx=5,pady=5)
button2 = ctk.CTkButton(root, text="2. Give me the best 3 restaurants based on my preferences",command=choice_rest) #restaurant basierend auf eingaben
button2.pack(padx=5,pady=5)
button3 = ctk.CTkButton(root, text="3. Give me a random restaurant in my city",command=random_rest) #zufälliges restaurant
button3.pack(padx=5,pady=5)

#Programm mit "destroy" beenden
quit_button = ctk.CTkButton(root, text="End Program", command=root.destroy)
quit_button.pack(padx=5,pady=5)

#Mainloop damit die fenster offen bleiben 
root.mainloop()
