# deloppgaver; g, h, i
import os


#opg g
class Sted:
    #opg g
    def __init__(self, id, navn, addresse, postnummer, poststed):
        self.id = id
        self.navn = navn
        self.addresse = addresse
        self.postnummer = postnummer
        self.poststed = poststed

    #opg g
    def __str__(self):
        return f"Sted med id {self.id}, navn {self.navn}, addresse {self.addresse}, postnummer {self.postnummer}, poststed {self.poststed}"


#opg h
def lag_sted():
    id = int(input("Skriv inn id til stedet: "))
    navn = input("Skriv inn hva stedet heter: ")
    addresse = input("Skriv inn addressen til stedet: ")
    postnummer = int(input("Skriv inn postnummered til stedet: "))
    poststed = input("Skriv inn poststedet til stedet: ")
    return Sted(id, navn, addresse, postnummer, poststed)


#opg i
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


#opg i
def skriv_sted_til_fil(fil, sted_liste):
    if os.path.exists(fil):
        print("Denne filen eksisterer allerede, overskriver")
        os.remove(fil)
    with open(fil, "w") as file:
        for sted in sted_liste:
            file.write(
                f"{sted.id};{sted.navn};{sted.addresse};{sted.postnummer};{sted.poststed}\n"
            )
