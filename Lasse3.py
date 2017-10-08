minListe = []

korer = True
while korer:
    elev = input("Indtast elevens navn: ")
    if (elev == ""):
        korer = False

    minListe.append(elev)

print(minListe)