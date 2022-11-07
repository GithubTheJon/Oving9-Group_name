
""" h """


class Sted:
    def __init__(self, id, stedsnavn, addresse=None, postnummer=None, poststed=None):
        self.id = id
        self.stedsnavn = stedsnavn
        self.addresse = addresse
        self.postnummer = postnummer
        self.poststed = poststed

    def __str__(self):
        return f"{self.id} {self.stedsnavn}, {self.addresse}, {self.postnummer}, {self.poststed}"


""" i """


def lag_sted():
    while 1 < 2:
        try:
            id = int(input("ID: "))
            stedsnavn = str(input("stedsnavn: "))
            addresse = str(input("Addresse: "))
            postnummer = int(input("Postnummer: "))
            poststed = str(input("Poststed: "))
        except ValueError:
            print("Ugyldig")
        else:
            break
    return Sted(id, stedsnavn, addresse, postnummer, poststed)


""" j """


if __name__ == "__main__":
    test = Sted('#113', 'Stavanger', "Stokka")
    print(test)
    print(lag_sted())


