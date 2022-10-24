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
        return self.tittel, self.sted, self.tid, self.varighet


av = Avtale("12", "Rom102", "2022-24-10 20:00:00", 30)
print(av.varighet)
