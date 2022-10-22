from encodings import utf_8
import random
import datetime
import json
#from tkinter.tix import Tree


class Igra():
    
    def __init__(self):
        self.trenutno_besedilo = ''
        self.zacetni_cas = ''
        self.koncni_cas = ''
        self.polje_povedi = []
        self.trenutni_indeks = 0

    def preberi_datoteko(self,datoteka):
        with open(datoteka,'r',encoding='utf-8') as f:
            besedilo = []
            vrstice = json.load(f)
            for i in vrstice:
                besedilo.append(i)
        return besedilo

    
    def nastavi_zacetni_cas(self):
        self.zacetni_cas = datetime.datetime.now()

    def izbor_random_crke(self):
        crke = 'ABCČDEFGHIJKLMNOPQRSŠTUVWXYZŽ'
        i = 0
        for i in range(20):
            self.polje_povedi.append(random.choice(crke))
        self.trenutno_besedilo = self.polje_povedi[0]
    
    def pravilnost_besed(self,vneseno_besedilo):
        if self.trenutno_besedilo == vneseno_besedilo:
            self.koncni_cas = datetime.datetime.now()
            self.naslednje_besedilo()
            return True
        else: return False

    def stetje_napak(besede):
        st_napak = 0
       # stetje napak preko definicije pravilnost_besed
        return st_napak

    def pripravi_besedilo(self, datoteka):
        besedilo = self.preberi_datoteko(datoteka)
        i = 0

        for i in range(len(besedilo)):
            self.polje_povedi.append(besedilo[i])

        self.trenutno_besedilo = self.polje_povedi[0]

    def nova_igra(self, tezavnost):
        self.polje_povedi = []
        self.trenutni_indeks = 0
        self.trenutno_besedilo = ''
        self.zacetni_cas = datetime.datetime.now()
        
        if tezavnost == 'zelo lahko':
            self.izbor_random_crke()
        elif tezavnost == 'lahko':
            self.pripravi_besedilo('./besedila/besedilo-lahko.json')
        elif tezavnost == 'srednje':
            self.pripravi_besedilo('./besedila/besedilo-srednje.json')
        elif tezavnost == 'težko':
            self.pripravi_besedilo('./besedila/besedilo-tezko.json')

    def naslednje_besedilo(self):
        self.trenutni_indeks += 1
        self.trenutno_besedilo = self.polje_povedi[self.trenutni_indeks]

    def konec_igre(self):
        if self.trenutni_indeks == len(self.polje_povedi):
            self.koncni_cas = datetime.datetime.now()

    def besede_na_minuto(self,cas):
        st_besed = 0
        seznam_besed = []
        for vrstica in self.polje_povedi:
            vrstica = vrstica.split()
            seznam_besed.append(vrstica)
        st_besed = len(seznam_besed)
        return int((st_besed / cas) * 60)


