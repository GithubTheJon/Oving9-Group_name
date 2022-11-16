# deloppgaver; c, d, e, f
import os


#opg c
class Kategori:

    def __init__(self, id, navn, prioritet=1):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet

    @staticmethod
    def method(self):
        return f'Kategorien med id {self.id}, navn {self.navn} og prioritet {self.prioritet}'

    def __str__(self):
        return f'Kategorien med id {self.id}, navn {self.navn} og prioritet {self.prioritet}'


#opg d
def lag_kategori():
    while 1 < 2:
        try:
            id = int(input("Skriv inn id til kategorien: "))
            navn = input("Skriv inn navnet til kategorien: ")
            prioritet = int(input("Skriv inn prioriteten til kategorien: "))
        except ValueError:
            print("Ugyldig")
        else:
            break
    return Kategori(id, navn, prioritet)


#opg e
def les_kategori_fra_fil(fil):
    if not os.path.exists(fil):
        print("Denne filen eksisterer ikke!")
        return
    leste_kategorier = []
    with open(fil, "r") as f:
        for linje in f:
            linje = linje.rstrip("\n")
            linje = linje.split(";")
            leste_kategorier.append(
                Kategori(int(linje[0]), linje[1], int(linje[2])))
    return leste_kategorier


#opg e
def skriv_kategori_til_fil(fil, kategori_liste):
    if os.path.exists(fil):
        print("Denne filen eksisterer allerede, overskriver")
        os.remove(fil)
    with open(fil, "w") as file:
        for kategori in kategori_liste:
            file.write(f"{kategori.id};{kategori.navn};{kategori.prioritet}\n")


#opg f
def skriv_ut_kategorier(kategori_liste):
    for index, kategori in enumerate(kategori_liste):
        print(f"id: {index}, kategori: {kategori}")
