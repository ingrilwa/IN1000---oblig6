"""
Oppgave 4, oblig 6 - Dato.py
Vi definerer klassen Dato, setter opp en konstruktør med variablene nyDag, nyMaaned og nyttAar. Deretter
definerer vi en metode lesAar som returnerer hvilket år det er. Neste metode lagDato lager og returner en dato
på en brukervennlig måte som er grei å lese. Metoden sjekkDag tar med seg et parameter, bestemtDag og kjører en
if-test som sjekker om dag - definert i konstruktør - er samme dag som den bestemte dagen. Heretter returneres
True eller False. Vi tester programmet i testDato.py.
"""
class Dato:
    def __init__ (self,nyDag,nyMaaned,nyttAar):
        self._dag=nyDag
        self._maned=nyMaaned
        self._aar=nyttAar

    def lesAar(self):
        return self._aar

    def lagDato(self):
        dato = "Datoen er: "+ str(self._dag) + "." + str(self._maned) + "." + str(self._aar)
        return dato

    def sjekkDag(self,bestemtDag):
        if self._dag == bestemtDag:
            return True
        else:
            return False
