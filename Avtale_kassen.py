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
    return Avtale(tittel, sted, starttidspunkt, varighet)


#  av = Avtale("12", "Rom102", "2022-24-10 20:00:00", 30)
#  print(av.varighet)
if __name__ == '__main__':
    avtale = lag_avtale()
    print(avtale)
