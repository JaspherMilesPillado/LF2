def berechnungsTypFunktion():
    berechnungsTyp = input("Möchtest du über Strecke(D) oder über Zeit(T) berechnen?\n ")[0]
    if berechnungsTyp[0] in "dD":
        print("Strecke ")
        return "d"

    elif berechnungsTyp[0] in "tT":
        print("Zeit ")
        return "t"

    else:
        print("ungültige Eingabe")
        berechnungsTypFunktion()


def streckenBerechnungsFunktion():
    strecke = float(input("Wie lang ist die Strecke? (in Km) \n "))
    intCheck = isinstance(strecke, float)

    if intCheck:
        return (strecke * 0.75)


def zeitBerechnungsFunktion():
    zeit = float(input("Wie lange fährst du? (in Minuten) \n "))
    intCheck = isinstance(zeit, float)
    if intCheck:
        return (zeit * 0.25)


if __name__ == '__main__':
    berechnungsTyp = berechnungsTypFunktion()

    if berechnungsTyp == "d":
        preis = streckenBerechnungsFunktion()

    elif berechnungsTyp == "t":
        preis = zeitBerechnungsFunktion()

    print("Es kostet: " + str(preis) + "€")
