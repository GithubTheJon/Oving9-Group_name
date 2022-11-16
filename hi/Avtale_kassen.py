import random
from datetime import datetime  # as dt
from kategori import Kategori as kategori
import sted


""" oppgave d"""


class Avtale:
    def __init__(self,
                 tittel: str,
                 sted: sted.Sted,
                 tid: datetime,
                 varighet: int,
                 kategori = []):
        self.tittel = tittel
        self.sted = sted
        self.tid = tid
        self.varighet = varighet
        self.kategorier = kategori

    # ubrukt
    def legg_til_kategori(self, kat):
        self.kategorier.append(kat)

    def __str__(self):
        return f"Avtalen heter {self.tittel},\n{self.sted},\nstarter {self.tid} og varer i {self.varighet} minutter,\n{self.kategorier}\n"


""" f """


def lag_avtale(avtale_liste, sted_liste):
    tittel = input("Skriv inn tittelen til avtalen: ")
    steds = sted.lag_sted(sted_liste)
    start_gyldig = False
    while not start_gyldig:
        try:
            aar = int(input("Skriv inn aaret avtalen skal holdes: "))
            maaned = int(input("Skriv inn maaneden avtalen skal holdes: "))
            dag = int(input("Skriv inn dagen avtalen skal holdes: "))
            time = int(input("Skriv inn timen avtalen skal holdes: "))
            minutt = int(input("Skriv inn minuttet avtalen skal holdes: "))
            starttidspunkt = datetime(aar, maaned, dag, time, minutt)
        except ValueError:
            print("Ugyldig dato!")
        else:
            start_gyldig = True
    varighet_gyldig = False
    while not varighet_gyldig:
        try:
            varighet = int(input("Skriv inn varigheten til avtalen: "))
        except ValueError:
            print("Ugyldig varighet!")
        else:
            varighet_gyldig = True
    avtale_liste.append(Avtale(tittel, steds, starttidspunkt, varighet))
    # print(Avtale(tittel, steds, starttidspunkt, varighet))
    return Avtale(tittel, steds, starttidspunkt, varighet)


""" g """


def avtaler_oversikt(avtale_liste):
    if len(avtale_liste) == 0:
        print("Det finnes ingen avtaler enda")
    else:
        for avtale in avtale_liste:
            index = 1
            print(f"Index: {index}, Tittel: {avtale.tittel}\n   {avtale}")
            index += 1


""" h """


def avtale_til_tekst_fil(fil, avtale_liste):
    print(f"skriv til: {fil}")
    with open(fil, "wt") as file:
        for avtale in avtale_liste:
            file.write(f"{avtale.tittel};{avtale.sted};{avtale.tid};{avtale.varighet};{avtale.kategorier}\n")


""" i """


def les_avtaler_fra_fil(fil):
    print(f"lest fra: {fil}")
    with open(fil, "r") as file:
        avtaler = []
        for linje in file:
            linje = linje.rstrip("\n")
            linje = linje.split(";")
            starttid = datetime.fromisoformat(linje[2])
            avtale_fra_fil = Avtale(linje[0], linje[1], starttid, linje[3], linje[4])
            avtaler.append(avtale_fra_fil)
        return avtaler


""" j """


def avtale_dato(listen, dato=0):
    # spørr om dato her istedet
    start_gyldig = False
    while not start_gyldig:
        try:
            ar = int(input("Skriv inn aaret avtalen skal holdes: "))
            ma = int(input("Skriv inn maaneden avtalen skal holdes: "))
            da = int(input("Skriv inn dagen avtalen skal holdes: "))
            dato = datetime.date(datetime(ar, ma, da))
        except ValueError:
            print("Ugyldig dato!")
        else:
            start_gyldig = True

    skjekk = 0
    for avtale in listen:
        if datetime.date(avtale.tid) == dato:
            print(avtale)
            skjekk += 1
    if skjekk == 0:
        print(f"Det er ingen avtaler denne dagen: {dato}")


def avtale_generator(antall, avtale_liste, sted_liste, kategori_liste):
    while antall > 0:
        tittel_list = ["Pizza", "Naboklage", "Toalett", "Airtime", "Kino", "President", "Studie", "Trening"]

        test_avtale = Avtale(tittel_list[random.randint(0, len(tittel_list) - 1)],
                             sted_liste[random.randint(0, len(sted_liste)-1)],
            datetime(2022, random.randint(1, 12), random.randint(1, 28), random.randint(8, 16), 15, 00),
                             random.randint(1, 6)*15, kategori_liste[random.randint(0, len(kategori_liste)-1)])
        avtale_liste.append(test_avtale)
        antall -= 1
    return avtale_liste


def sted_generator(antall, sted_liste):
    i = 0
    while antall > 0:
        gate_tall = random.randint(1, 99)
        addresse_liste = [f"Svingsgata {gate_tall}", f"Haugelandgata {gate_tall}", f"Sandsgaardsveien {gate_tall}"]
        stedet = sted.Sted(i, addresse_liste[random.randint(0, len(addresse_liste)-1)], "", random.randint(1000, 9999), "")
        sted_liste.append(stedet)
        antall -= 1
        i += 1
    return sted_liste


def kategori_generator(antall, kategori_liste):
    i = 0
    while antall > 0:
        grad = [f"*Viktig*", f"*Møte*", f"*Innen*"]
        kagori = kategori(i, grad[random.randint(0, len(grad)-1)], random.randint(1, 10))
        kategori_liste.append(kagori)
        antall -= 1
        i += 1
    return kategori_liste


"""
if __name__ == '__main__':
    avtale_liste = []
    sted_liste = []
    fil = "readme.txt"

    sted_generator(10, sted_liste)
    avtale_generator(10, avtale_liste, sted_liste)
    les_avtaler_fra_fil(fil)
    avtale_til_tekst_fil(fil, avtale_liste)
    les_avtaler_fra_fil(fil)

    # avtaler_oversikt()

    # avtaler_fra_fil = les_avtaler_fra_fil("readme.txt")
    # print(avtaler_fra_fil)

    # avtale_dato(avtale_liste)
    # skriv 2022, 10, 28
"""
