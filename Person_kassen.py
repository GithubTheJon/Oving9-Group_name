class Person:
    def __init__(self, id, navn, tlf, epost):
        self.id = id
        self.navn = navn
        self.tlf = tlf
        self.epost = epost

    def __str__(self):
        return f"ID: {self.id}, Navn: {self.navn},tlf: {self.tlf}, epost: {self.epost}"



