"""
Testprogram for dato.py. Oppgave 4, oblig 6
Først importerer vi klassen Dato fra dato.py. Deretter definerer vi igjen vårt hovedprogram. vi lager et objekt
dato, kaller på klassen Dato med en valgt dato som parameter. Deretter printer vi ut året i denne datoen ved
hjelp av metoden lesAar som vi samtidig kaller på. Da printes kun året i datoen ut. Så kjører vi en if-test som
sjekker om datoen er akkurat den 15, ved hjelp av metoden sjekkDag og parameteren 15. Hvis det er dette, printes
"lønningsdag!" ut, hvis ikke printes "ny måned, nye muligheter" ut. Vi definerer en variabel dato_brukervennlig
som kjører objektet dato gjennom metoden lagDato og datoen printes da ut på en grei, lesbar måte.
Til slutt kaller vi på hovedprogrammet.
"""
from dato import Dato

def hovedprogram():
    dato = Dato(15,10,2001)
    print(dato.lesAar())
    if dato.sjekkDag(15):
        print("Loennningsdag!")
    else:
        print("Ny maaned, nye muligheter")
    dato_brukervennlig = dato.lagDato()
    print(dato_brukervennlig)

hovedprogram()
