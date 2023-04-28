"""
Testprogram for hund.py, oppgave 3, oblig 6
Vi importerer først klassen Hund fra hund.py. Deretter definerer vi vårt hovedprogram, slik som i forrige
oppgave om motorsykler. Inne i hovedprogrammet lager vi et objekt labrador som kaller på klassen Hund og tar
med seg variablene 6 og 30 som tilsvarer alder og vekt. Vi kaller så på metoden spring gjennom labrador-objektet.
Deretter printer vi ut vekten til objektet ved hjelp av metoden hentVekt. Så kaller vi på metoden spis med
5 som variabel og printer igjen ut vekten med hentVekt. Dette gjør vi to ganger til, med spring og spis før vi
henter ut vekten. Til slutt kaller vi på hovedprogrammet.
"""
from hund import Hund

def hovedprogram():
    labrador = Hund(6,30)
    labrador.spring()
    print(labrador.hentVekt())
    labrador.spis(5)
    print(labrador.hentVekt())
    labrador.spring()
    print(labrador.hentVekt())
    labrador.spis(3)
    print(labrador.hentVekt())

hovedprogram()
