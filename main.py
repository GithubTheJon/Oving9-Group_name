import Avtale_kassen as avtale

if __name__ == "__main__":
    fil = "readme.txt"

    kjor = True
    avtale_liste = []
    avtale.avtale_generator(10, avtale_liste)

    while kjor:
        print("\nVelg et valg fra menyen:")
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
            print(f"Leser avtaler fra {fil}\n")
            leste_avtaler = avtale.les_avtaler_fra_fil(fil)
            if leste_avtaler:
                for lest in leste_avtaler:
                    avtale_liste.append(lest)
                    print(lest)

        elif valg == 2:
            print(f"Skriver avtaler til {fil}")
            print(avtale.avtale_til_tekst_fil(fil, avtale_liste))

        elif valg == 3:
            ny_avtale = avtale.lag_avtale(avtale_liste)
            avtale_liste.append(ny_avtale)
            print("Laget avtalen:")
            print(ny_avtale)

        elif valg == 4:
            print("Skriv inn hvilken indeks som skal slettes: ")
            for i in range(len(avtale_liste)):
                print(f"Indeks: {i}, avtale: {avtale_liste[i]}")
            valg_indeks = int(
                input("Skriv inn indexfcn til avtalen du vil slette: "))
            avtale_liste.pop(valg_indeks)

        elif valg == 5:
            print("Skriv inn hvilken avtale du vil redigere (erstatte): ")
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
            break
        else:
            print("Hva har du gjort?")
    print("Avsluttet! Vellykket!")
