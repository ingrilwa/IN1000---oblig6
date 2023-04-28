"""
Oppgave 3, oblig 6.
Vi definerer klassen Hund og fyller klassen med konstruktør og metoder. konstrukøren har parameterne alder
og vekt. Vi tar også med oss den faste variabelen metthet og setter den lik 10. Deretter definerer vi metoden
hentAlder, tar med oss self og returnerer alderen. Neste metode gjør det samme, bare med vekt i hentVekt.
Deretter definerer vi metoden spring som minsker metthet med 1. Så foretar vi en if test som da sjekker om
metthet er mindre enn 5 og hvis den er dette, minsker også vekten. Metoden spis tar med seg et heltall som
legges til metthet. Deretter skriver vi en if test som øker vekten til hunden med 1 hvis mettheten er over 7.
Vi tester dette programmet i testHund.py
"""
class Hund:
    def __init__ (self,alder,vekt) :
        self._alder=alder
        self._vekt=vekt
        self._metthet=10

    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return self._vekt

    def spring(self):
        self._metthet-=1
        if self._metthet < 5:
            self._vekt-=1

    def spis(self,heltall):
        self._metthet+= heltall
        if self._metthet > 7:
            self._vekt+=1
