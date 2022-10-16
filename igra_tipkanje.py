from encodings import utf_8
import random
import datetime

class Igra():
    
    def __init__(self,besedilo):
        self.besedilo = besedilo
        self.zacetni_cas = ''
        self.koncni_cas = ''
    
    def nastavi_zacetni_cas(self):
        self.zacetni_cas = datetime.datetime.now()

    def izbor_random_crke():
        crke = 'ABCČDEFGHIJKLMNOPQRSŠTUVWXYZŽ'
        crka = random.choice(crke)
        return crka
    
    def pravilnost_besed(self,vnesena_beseda):
        if self.besedilo == vnesena_beseda:
            self.koncni_cas = datetime.datetime.now()
            return True
        else: return False

    def stetje_napak(besede):
        st_napak = 0
       # stetje napak preko definicije pravilnost_besed
        return st_napak

def prebereri_vrstice(datoteke):
    datoteka = random.choice(datoteke)
    with open(datoteka,'r',encoding=utf_8) as f:
        vrstice = f.readLines()
        for vrstica in vrstice:
            print(vrstica)
    
def besede_na_minuto(st_besed,cas):
    return int((st_besed / cas) * 60)






