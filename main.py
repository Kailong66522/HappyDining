import pandas as pd
import random
import tkinter as tk 



excel_file_1 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhi.xlsx"
df1 = pd.read_excel(excel_file_1)
print("Welcome to Kais Dining Experience in New Delhi")
print("Please choose from the Following:")

print("1. Give me the best restaurant in the city")
print("2. Give me the best restaurant thats specialized in a certain cuisine")
print("3. Give me a random restaurant in my city")
choice = int(input("Please choose between the options!\n>"))
#Das beste Restaurant wählen
if choice == 1:
  print("The best restaurant in the city is: ")
  max_index = df1['Z-number'].idxmax()
# Extract the entire row associated with the maximum value
  max_row = df1.loc[max_index]
  print(max_row)


#Ein bestimmtes Restaurant wählen
elif choice == 2:
  # Hier hat man am Anfang eine eigene Angabe, später mit dem User Interface hätte ich gerne eine Liste durch die man Scrollen kann und dann drauf klicken kann um zu wählen
  print("What cuisine should the Restaurant have?")
  Cuisine = input("\n>")
  Cuisine2 = df1['Cuisines'] == Cuisine
  print("How much Indian Rupees do you want to spend for two?")
  Rupees = int(input("\n>"))
  Rupees2 = df1['Average Cost for two'] < Rupees
  print("How many Stars should the Restaurant have?")
  print("1. 5 Stars")
  print("2. 4 or more Stars")
  print("3. 3 or more Stars")
  print("4. 2 or more Stars")
  print("5. 1 or more Stars")
  print("6. It can be a new not rated Restaurant")
  stars = int(input("Please choose between the options!\n>"))
  if stars == 1:
    Rating = df1['Rating star'] == 5
  elif stars == 2:
    Rating = df1['Rating star'] >= 4
  elif stars == 3:
    Rating = df1['Rating star'] >= 3
  elif stars == 4:
    Rating = df1['Rating star'] >= 2
  elif stars == 5:
    Rating = df1['Rating star'] >= 1
  elif stars == 6:
    Rating = df1['Rating star'] >= 0
  #print(Rating)
  print("Do you wish to have the food delivered or go to the restaurant?")
  print("1. Delivered")
  print("2. Go to restaurant")
  deliver = int(input("Please choose between the options!\n>"))
  if deliver == 1:
    Deliver = df1['Has Online delivery'] == 'Yes'
    filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Deliver)]
    sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
    if len(sorted_df) >= 3:
     first_three_rows = sorted_df.head(3)
    else:
     first_three_rows = sorted_df
    print("Here are the 3 best restaurants based on your preferences")
    print(first_three_rows)
  elif deliver == 2:
    Deliver = df1['Has Online delivery'] == 'No'
    print("Would you like to Book a Table for your visit?")
    booking = input("\n>")
    if booking == 'yes':
      Booking = df1['Has Table Booking'] == 'Yes'
      filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
      sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
      if len(sorted_df) >= 3:
        first_three_rows = sorted_df.head(3)
      else:
        first_three_rows = sorted_df
      print("Here are the 3 best restaurants based on your preferences")
      print(first_three_rows)
    elif booking == 'no':
      Booking = df1['Has Table Booking'] == 'No'
      filtered_df1 = df1[(Rating) & (Cuisine2) & (Rupees2) & (Booking) & (Deliver)]
      sorted_df = filtered_df1.sort_values(by='Z-number', ascending=False)
      if len(sorted_df) >= 3:
        first_three_rows = sorted_df.head(3)
      else:
        first_three_rows = sorted_df
      print("Here are the 3 best restaurants based on your preferences")
      print(first_three_rows)



#Random Restaurant wählen 
elif choice == 3:
  print("Heres a random restaurant in your city: ")
  num_rows = len(df1)
  random_index = random.randint(0, num_rows - 1)
  random_row = df1.iloc[random_index]
  print(random_row)
#print(df1.columns)
# print(df1)

#Alle Ratings ausgeben von Anfang bis Ende
# filtered_df1 = df1.loc[:, 'Rating text']
# print(filtered_df1)
#Nur Restaurants mit der Bewertung Good + mehr als 90 Votes + Gewichtung größer 6 ausgeben
#filtered_df1 = df1[(df1['Rating text'] == "Good") & (df1['Votes'] > 90) & (df1['Gewichtung'] > 6)] 
# print(filtered_df1)
#print(filtered_df1['Restaurant Name'])
#print(filtered_df1['Adress'])
# pd.read_excel(r'"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\Archive Link 1 Tabelle Restaurants.csv"', engine='openpyxl')

# Hier kann mit der Variable Rating etwas ausgegeben werden
#filtered_df1 = df1[(Rating) & (df1['Votes'] > 90) & (df1['Gewichtung'] > 6)]
 # print(filtered_df1)
