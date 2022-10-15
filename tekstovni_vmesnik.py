import igra_tipkanje

def start(cas):
    navodila = f'Na voljo imaš {cas}s da natipkaš čim več besed. Za začetek igre klikni gumb Start.'  
    print(navodila)

def konec():
    print('Konec igre. Čas se je iztekel!')

def statistika(cas,st_besed):
    #st_napak = igra_tipkanje.Igra.stetje_napak(besede)
    wpm = igra_tipkanje.Igra.besede_na_minuto(st_besed,cas)
    if wpm >= 40:
        print(f"Bravo! \nTvoje povprečno število natipkanih besed na minuto(wpm) je {wpm}. \nPovrečen človek ima 40wpm")
    else:
        print(f"Tvoje povprečno število natipkanih besed na minuto(wpm) je {wpm}. \nPovprečen človek ima 40wpm")


