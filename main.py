import Avtale_kassen as avtale

if __name__ == "__main__":
    kjor = True
    avtale_liste = []
    while kjor:
        print()
        print("Velg et valg fra menyen:")
        print("1: for les avtaler fra fil")
        print("2: for skriv avtaler til fil")
        print("3: Skriv inn ny avtale")
        print("4: Slett avtale fra listen")
        print("5: Rediger avtale (erstatt)")
        print("0: Skriv ut alle avtaler og avslutt")
        valg = -1
        gyldig_valg = False
        while not gyldig_valg:
            try:
                valg = int(input("Ditt valg: "))
            except ValueError:
                print("Ugyldig valg!")
            else:
                gyldig_valg = True
        if valg == 1:
            print("Leser avtaler fra avtaler.txt")
            leste_avtaler = avtale.les_avtaler_fra_fil("avtaler.txt")
            if leste_avtaler:
                for lest in leste_avtaler:
                    avtale_liste.append(lest)
        elif valg == 2:
            print("Skriver avtaler til avtaler.txt")
            avtale.lagre_avtaler_til_fil(avtale_liste)
        elif valg == 3:
            ny_avtale = avtale.lag_avtale()
            avtale_liste.append(ny_avtale)
            print("Lager avtalen:")
            print(ny_avtale)
        elif valg == 4:
            print("Skriv inn hvilken indeks som skal slettes: ")
            if avtale_liste:
                for i in range(len(avtale_liste)):
                    print(f"Indeks: {i}, avtale: {avtale_liste[i]}")
            valg_indeks = int(
                input("Skriv inn indeksen til avtalen du vil slette: "))
            avtale_liste.pop(valg_indeks)
        elif valg == 5:
            print("Skriv inn hvilken avtale du vil redigere (erstatte): ")
            if avtale_liste:
                for i in range(len(avtale_liste)):
                    print(f"Indeks: {i}, avtale: {avtale_liste[i]}")
            valg_indeks = int(
                input(
                    "Skriv inn indeksen til avtalen du vil redigere (erstatte): "
                ))
            print(f"{avtale_liste[valg_indeks]} slettet!")
            print("Lag avtalen som skal erstatte den slettede avtalen: ")
            ny_avtale = avtale.lag_avtale()
            avtale_liste[valg_indeks] = ny_avtale
        elif valg == 0:
            print("Avtaler:")
            if avtale_liste:
                for a in avtale_liste:
                    print(a)
            kjor = False
        else:
            print("wat?")
    print("Avsluttet!")
