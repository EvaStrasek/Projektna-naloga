from encodings import utf_8
import random
import time

class Igra():
    
    def __init__(self,beseda,barva):
        self.beseda = beseda
        self.barva = barva
    
    def izbor_random_crke():
        crke = 'ABCČDEFGHIJKLMNOPQRSŠTUVWXYZŽ'
        crka = random.choice(crke)
        return crka

    def igra(self):
        crka = self.izbor_random_crke()
        pravilno = 0
        while self.casovnik(90):
            vtipkana_crka = input('Vpisi črko').split().upper()
            if vtipkana_crka == crka:
                pravilno += 1
                crka = self.izbor_random_crke()
        print(pravilno)
    
    def pravilnost_besed(beseda):
        return input('>') == beseda

    def stetje_napak(besede):
        st_napak = 0
        while input('>') == besede:
            st_napak += 1
        return st_napak

    def prebereri_vrstice(datoteka):
        with open(datoteka,'r',encoding=utf_8) as f:
            vrstice = f.readLines()
            for vrstica in vrstice:
                print(vrstica)

    def casovnik(cas):
        while cas > 0:
            time.sleep(1)
            cas -= 1
        print('Čas se je iztekel. Igre je konec')
    
    def besede_na_minuto(st_besed,cas):
        return int((st_besed / cas) * 60)






