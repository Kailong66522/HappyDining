# HappyDining
Seminararbeit Kai Hinrichs

Bevor du den Code ausführen willst, solltest du diese Bibliotheken installieren, falls sich das alles nicht installieren lässt oder irgendwo Fehler sind, rate ich dir, dass einzeln immer mit pip(pip3) install xyz zu machen.

pip install scikit-learn matplotlib gower pandas 
pip3 install customtikinter tkintermapview

Diese Bibliotheken sind Voraussetzung für die Funktion des Codes.

Ebenso muss die Excel-Tabelle mit dem Inhalt der Restaurants aus NewDelhi zusammen mit dem Code gespeichert werden, und der Speicherpfad im Code beim Auslesen der Excel Tabelle auf deinen Pfad geändert werden.
Das ist im Code bei den obersten zeilen zu ändern: 

excel_file_2 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhiwahlgross.xlsx"
excel_file_1 = r"C:\Users\kainu\OneDrive\Desktop\Seminararbeit\RestaurantsNewDelhi.xlsx"


