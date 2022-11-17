# from Oving10 import Avtale_kassen as Avtale
import Avtale_kassen as Avtale
import kategori
import sted

if __name__ == "__main__":
    avtale_fil = "avtalerfilen.txt"

    avtale_liste = []
    kategori_liste = []
    sted_liste = []

    Avtale.kategori_generator(10, kategori_liste)
    Avtale.sted_generator(10, sted_liste)
    Avtale.avtale_generator(10, avtale_liste, sted_liste, kategori_liste)

    # sted.sted_generator(10, sted_liste)

    while 2 > 1:
        print("\nVelg et valg fra menyen:")
        print("1: Avtaler")
        print("2: Kategorier")
        print("3: Steder")
        print("0: Avslutt")
        h_valg = -1
        gyldig_valg = False
        while not gyldig_valg:
            try:
                h_valg = int(input("Ditt valg: "))
            except ValueError:
                print("Ugyldig valg!")
            else:
                gyldig_valg = True

        if h_valg == 1:
            kjor_av_avtaler = True
            while kjor_av_avtaler:
                print("\nVelg fra Avtaler menyen:")
                print("1: Les avtaler fra fil")
                print("2: Skriv avtaler til fil")
                print("3: Skriv inn ny avtale")
                print("4: Slett avtale fra listen")
                print("5: Rediger avtale (erstatt)")
                print("6: Finn Avtale etter Sted")
                print("0: Gå tilbake")
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
                    print(f"Leser avtaler fra {avtale_fil}\n")
                    leste_avtaler = Avtale.les_avtaler_fra_fil(avtale_fil)
                    avtale_liste = []
                    if leste_avtaler:
                        for avtale in leste_avtaler:
                            avtale_liste.append(avtale)
                    print(f"Filen {avtale_fil} har blitt lest")
                    print(avtale_liste)

                elif valg == 2:
                    print(f"Skriver avtaler til {avtale_fil}")
                    Avtale.avtale_til_tekst_fil(avtale_fil, avtale_liste)

                elif valg == 3:
                    ny_avtale = Avtale.lag_avtale(avtale_liste, sted_liste)
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
                    ny_avtale = Avtale.lag_avtale(avtale_liste, sted_liste)
                    avtale_liste[valg_indeks] = ny_avtale

                elif valg == 6:
                    print("Skriv inn stedet eller velg fra index")
                    print("1: velg index")
                    print("2: skriv inn selv")
                    f_valg = int(input("Velg: "))
                    if f_valg == 1:
                        for sted in sted_liste:
                            print(sted)
                        ids = int(input("velg indexen: "))
                        for avtale in avtale_liste:
                            if avtale.sted.id == ids:
                                print(avtale)
                    elif f_valg == 2:
                        sted.les_sted_fra_fil(sted_liste)

                elif valg == 0:
                    kjor_av_avtaler = False
                    break
                else:
                    print("Hva har du gjort?")
            print("*Gikk tilbake*")
            h_valg = -1


        elif h_valg == 2:
            kjor_av_kategorier = True
            while kjor_av_kategorier:
                print("\nVelg fra Kategorier menyen:")
                print("1: lag en ny kategori")
                print("2: Legg til kategori til en avtale")
                print("3: Print kategori listen")
                print("0: Gå tilbake")
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
                    ny_kategori = kategori.lag_kategori()
                    kategori_liste.append(ny_kategori)
                    print("Laget kategorien:")
                    print(ny_kategori)

                # Her er Oppgave O
                elif valg == 2:
                    i = 0
                    print("\nVelg hvilken Avtale etter Index:")
                    for avtale in avtale_liste:
                        print(f"Index {i}: {avtale}")
                        i += 1
                    indexen_avtale = int(input("Velg Index for Avtale (int): "))

                    for kategori in kategori_liste:
                        print(kategori)
                    print("Velg hvilken Kategori etter id")
                    index_kat = int(input("Velg id for Kategori (int): "))

                    # fikset opg o
                    avtale_liste[indexen_avtale].kategorier.append(kategori_liste[index_kat])
                    print(f"{avtale_liste[indexen_avtale].tittel} har kategoriene: ")
                    for kat in avtale_liste[indexen_avtale].kategorier:
                        print(kat)

                    # hva er dette?
                    # Kategorien som skal legges til
                    # kat = kategori_liste[index_kat].method(kategori)
                    # Kategorien som allerede er lagt til
                    # k = f"{avtale_liste[indexen_avtale].kategorier}"

                    # kk = [k, kat]

                    # for avtale in avtale_liste:
                    #     if avtale == avtale_liste[indexen_avtale]:
                    #         pass
                    #         avtale_liste[indexen_avtale].kategorier = kk
                    # print(avtale_liste[indexen_avtale])

                elif valg == 3:
                    for kategori in kategori_liste:
                        print(kategori)

                elif valg == 0:
                    kjor_av_avtaler = False
                    break
                else:
                    print("Hva har du gjort?")
            print("*Gikk tilbake*")
            h_valg = -1


        elif h_valg == 3:
            kjor_av_steder = True
            while kjor_av_steder:
                print("\nVelg fra Steder menyen:")
                print("1: legg til nytt sted: ")
                print("2: Print steds listen")
                print("0: Gå tilbake")
                valg = -1
                gyldig_valg = False
                while not gyldig_valg:
                    try:
                        valg = int(input("Ditt valg: "))
                    except ValueError:
                        print("Ugyldig valg!")
                    else:
                        gyldig_valg = True

                # sted
                if valg == 1:
                    nytt_sted = sted.lag_sted(sted_liste)
                    sted_liste.append(nytt_sted)
                    print(f"La til {nytt_sted} i steder")

                if valg == 2:
                    for sted in sted_liste:
                        print(sted)

                elif valg == 0:
                    kjor_av_avtaler = False
                    break
                else:
                    print("Hva har du gjort?")
            print("*Gikk tilbake*")
            h_valg = -1

        # deloppgave p
        elif h_valg == 4:
            pass


        elif h_valg == 0:
            kjor = False
            break

    print("*Avsluttet*")
