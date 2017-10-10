minAndenListe = []
viKorer = True

while viKorer:
    minInput =input('Indast navn ')
    if (minInput == ''):
        viKorer = False
    else:

         minAndenListe.append(minInput)



print(minAndenListe)