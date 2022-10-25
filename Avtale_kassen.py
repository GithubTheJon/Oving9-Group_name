from datetime import datetime  # as dt
""" oppgave d"""


class Avtale:

    def __init__(self, tittel: str, sted: str, tid: datetime, varighet: int):
        self.tittel = tittel
        self.sted = sted
        self.tid = tid
        self.varighet = varighet

    """ e """

    def __str__(self):
        return f"Denne avtalen heter {self.tittel}, er i {self.sted}, starter {self.tid} og varer i {self.varighet} minutter"


""" f """


def lag_avtale():
    tittel = input("Skriv inn tittelen til avtalen: ")
    sted = input("Skriv inn hvor avtalen skal holdes: ")
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
    avtale_liste.append(Avtale(tittel, sted, starttidspunkt, varighet))
    return Avtale(tittel, sted, starttidspunkt, varighet)


""" g """


def avtaler_oversikt(oversikt=0):
    if len(avtale_liste) == 0:
        print("Det finnes ingen avtaler enda")
    else:
        for avtale in avtale_liste:
            index = 1
            print(f"Index: {index}, Tittel: {avtale.tittel}\n   {avtale}")
            index += 1


""" h """


def avtale_til_tekst_fil():
    with open("readme.txt", "w") as file:
        for avtale in avtale_liste:
            file.write(
                f"{avtale.tittel};{avtale.sted};{avtale.tid};{avtale.varighet}\n"
            )
            #  index = 1
            #  file.write(f"Index: {index}\n   {avtale}")
            #  file.write("\n")
            #  index += 1


""" i """


def les_avtaler_fra_fil(fil):
    avtaler = []
    with open(fil, "r") as f:
        for linje in f:
            linje = linje.rstrip("\n")
            linje = linje.split(";")
            starttid = datetime.fromisoformat(linje[2])
            avtale_fra_fil = Avtale(linje[0], linje[1], starttid,
                                    int(linje[3]))
            avtaler.append(avtale_fra_fil)
    return avtaler


if __name__ == '__main__':
    avtale_liste = []
    test_avtale = Avtale("test", "Rom102", datetime(2022, 10, 25, 15, 30, 00),
                         60)
    avtale_liste.append(test_avtale)

    # avtale = lag_avtale()
    # print(avtale)
    avtaler_oversikt()

    avtale_til_tekst_fil()
    avtaler_fra_fil = les_avtaler_fra_fil("readme.txt")
    print(avtaler_fra_fil[0])
