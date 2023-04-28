"""
Fortsettelse/testprogram for oppgave 1, oblig 6
Dette programmet tester klassen motorsykkel, lagd i motorsykkel.py. Først importerer vi klassen Motorsykkel.
Deretter definerer vi et hovedprogram. Det inneholder tre motorsykkelobjekter, som jeg kalte sykkel1, sykkel2
og sykkel3. Disse har merke, registreringsnummer og kilometerstand som egenskaper. Deretter følger vi oppgaven
og skriver ut sykkel1, 2 og 3, før vi "kjører" motorsykkel 3 mer, slik at gjennom instansmetoden kjor, øker
kilometerstanden med 10 kilometer. Derfor skriver vi ut objektet for sykkel 3 på nytt, ved hjelp av metoden
skrivUt. Da ser vi at kilometerstanden har økt med 10. Til slutt kaller vi hovedprogrammet.
"""
from motorsykkel import Motorsykkel

def hovedprogram():
    sykkel1 = Motorsykkel("Yamaha","LS0934",5000 )
    sykkel2 = Motorsykkel("Honda","BA8597",1800)
    sykkel3 = Motorsykkel("BMW","FS9925",500 )
    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()
    sykkel3.kjor(10)
    sykkel3.skrivUt()

hovedprogram()
