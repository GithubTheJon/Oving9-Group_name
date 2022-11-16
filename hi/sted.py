# Deloppgaver; g, h, i
import os


# opg g
class Sted:
    # opg g
    def __init__(self, id, navn, addresse = 0, postnummer = 0, poststed = 0):
        self.id = id
        self.navn = navn
        self.addresse = addresse
        self.postnummer = postnummer
        self.poststed = poststed

    # opg g
    def __str__(self):
        return f"Sted med id {self.id}, navn {self.navn}, addresse {self.addresse}, postnummer {self.postnummer}, poststed {self.poststed}"


# opg h
def lag_sted(sted_liste):
    valg = -1
    print("Et sted er nødvendig")
    print("1: lag nytt sted: ")
    print("2: velg et sted: ")
    valg = int(input("Velg: "))
    if valg == 1:
        start_gyldig = False
        while not start_gyldig:
            try:
                ids = int(input("Skriv inn id til stedet: "))
                navn = input("Skriv inn hva stedet heter: ")
            except ValueError:
                print("Ugyldig!")
            else:
                start_gyldig = True
        return Sted(ids, navn)

    elif valg == 2:
        i = 0
        for sted in sted_liste:
            print(f"index {i}; {sted}")
            i += 1
        stedet = int(input("Velg en index: "))
        print(f"Valgte: {sted_liste[stedet]}")
        return sted_liste[stedet]


# opg i
def les_sted_fra_fil(fil):
    if not os.path.exists(fil):
        print("Denne filen eksisterer ikke!")
        return
    leste_steder = []
    with open(fil, "r") as f:
        for linje in f:
            linje = linje.rstrip("\n")
            linje = linje.split(";")
            sted = Sted(int(linje[0]), linje[1], linje[2], linje[3], linje[4])
            leste_steder.append(sted)
    return leste_steder


# opg i
def skriv_sted_til_fil(fil, sted_liste):
    if os.path.exists(fil):
        print("Denne filen eksisterer allerede, overskriver")
        os.remove(fil)
    with open(fil, "w") as file:
        for sted in sted_liste:
            file.write(
                f"{sted.id};{sted.navn};{sted.addresse};{sted.postnummer};{sted.poststed}\n"
            )
