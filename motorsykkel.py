"""
Oppgave 1, oblig6.
Definerer en klasse motorsykkel. Konstruktøren defineres så med merke, registreringsnummer og kilometerstand som parametere. Videre defineres instansmetoder kjør, hentKilometerstand og skriv ut. De har som alltid, self som parameter, i tillegg til de passende egenskapene. kjør øker kilometerstanden med gitte antall kilometer. hentKilometerstand returnerer motorsyklenes totale kilometerstand, og skrivUt skriver ut alle disse egenskapene, merke, registreringsnummer og kilometerstand. Neste del av oppgaven er filen testMotorsykkel.py.
"""
class Motorsykkel:
    def __init__ (self,merke,regnr,km):
        self._merke=merke
        self._regnr=regnr
        self._km=km

    def kjor(self,km):
        self._km+=km

    def hentKilometerstand(self):
        return self._km

    def skrivUt(self):
        print("merke:", self._merke)
        print("registreringsnummer:", self._regnr)
        print("kilometer:", self._km)
