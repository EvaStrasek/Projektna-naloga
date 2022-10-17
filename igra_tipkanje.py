from encodings import utf_8
import random
import datetime



class Igra():
    
    def __init__(self,besedilo):
        self.besedilo = besedilo
        self.zacetni_cas = ''
        self.koncni_cas = ''

    def preberi_datoteko(datoteka):
        with open(datoteka,'r',encoding='utf-8') as f:
            besedilo = []
            vrstice = f.load()
            for i in vrstice:
                besedilo.append(i)
        return besedilo

    
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


class Tipkanje():
    def __init__(self):
        self.igre = []
        self.trenutna_igra = 0 
        self.st_besed_v_povedi = 0
        self.st_vrstic = 0
    
    def igra(self,st_besed_v_povedi,st_vrstic):
        self.igre = []
        self.trenutna_igra = 0
        self.st_besed_v_povedi = st_besed_v_povedi
        self.st_vrstic = st_vrstic

        i = 0
        while i < st_vrstic:
            igra = Igra.igra(st_besed_v_povedi)
            self.igre.append(igra)
            i += 1
        return self.trenutna_igra
    
def besede_na_minuto(st_besed,cas):
    return int((st_besed / cas) * 60)





