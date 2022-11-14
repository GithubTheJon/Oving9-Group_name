import Avtale_kassen as avtale
import kategori
import sted

if __name__ == "__main__":
    avtale_fil = "avtale.txt"
    kategori_fil = "kategori.txt"
    sted_fil = "sted.txt"


    kjor = True
    avtale_liste = []
    kategori_liste = []
    sted_liste = []

    # avtale.avtale_generator(10, avtale_liste)
    # person.person_generator(10, person_liste)
    # sted.sted_generator(10, sted_liste)

    while kjor:
        print("\nVelg et valg fra menyen:")
        print("1: Les avtaler fra fil")
        print("2: Skriv avtaler til fil")
        print("3: Skriv inn ny avtale")
        print("4: Slett avtale fra listen")
        print("5: Rediger avtale (erstatt)")
        print("6: Legg til kategori")
        print("7: Legg til sted")
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

        elif valg == 6:
            ny_kategori = kategori.lag_kategori()
            kategori_liste.append(ny_kategori)
            print(f"La til {ny_kategori} i kategorier")

        elif valg == 7:
            nytt_sted = sted.lag_sted()
            sted_liste.append(nytt_sted)
            print(f"La til {nytt_sted} i steder")

        elif valg == 0:
            print("Avtaler:")
            if len(avtale_liste) > 0:
                for a in avtale_liste:
                    print(a)
            kjor = False
            break
        else:
            print("Hva har du gjort?")
    print("Avsluttet! Vellykket!")
