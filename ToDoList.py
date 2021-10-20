# Eine To-Do-Liste -- Christina Zmugg


   
def menue(): 
    print ("-- Wilkommen bei Ihrer To-Do-Liste --")
    print ("Druecken Sie die ....")
    print ("1) um zu sehen was auf Ihrer To-Do-Liste steht,")
    print ("2) um etwas in die Liste einzutragen,")
    print ("3) um etwas Erledigtes zu loeschen,")
    print ("4) Zeitaufwand (in Minuten) ausgeben,")
    print ("5) Anzahl der Einträge ausgeben,")
    print ("6) gesamte Liste löschen,")
    print ("7) um das Prgramm zu verlassen,")

menue()

list = []

while True:
    print ("- - - - - - - - - - - - - - - - - - - -")
    option = input("Geben Sie eine der Zahlen ein! ")
    if option == '1':
        if len(list) > 0:
            ("Ihre TODO-List:")
            i = 0
            for item in list:
                print (i+1, ": ",list[i])
                i += 1
        else:
            print ("Die ToDo-List ist momentan noch leer!") 
    elif option == '2':   
        list.append(input("Geben Sie einen neuen Eintrag in ihre Liste ein: ") )
    elif option == '3':
        index = int(input("Geben Sie die Nummer des Eintrages ein, welchen Sie aus der Liste löschen wollen: "))
        if(len(list) >= index):
            i = 0
            for item in list:
                if index-1 == i:
                    list.pop(i)  
                i+=1
        else:
            print("Eintrag mit dieser Nummer exestiert nicht!")
    
    elif option == '4':
        min = int(input("Geben Sie die ungefaehre Zeit (in Minuten) an, die Sie für das Erledigen eines Eintrages benötigen: "))
        zeit = min * len(list)
        print("Sie werden ungefaehr ", zeit, "Minuten benötigen um alle Einträge der TODO-List zu erledigen!")
    elif option == '5':
        print("Es sind ", len(list), " Einträge vorhanden")      
    elif option == '6':
        list.clear()
        print("Ihre Liste ist gelöscht.")
    elif option == '7':
        print("Auf Wiedersehen!")  
        break
    else:
        print("Falsche Eingabe!")             

        
   