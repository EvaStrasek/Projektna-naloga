from encodings import utf_8
import random
import datetime
import json
import os



DATOTEKA_Z_REKORDI = 'rekordi.json'

class Stanje():

    def __init__(self):
        self.igre = {}

    def nova_igra(self, uporabnisko_ime, tezavnost):
        igra = Igra()
        igra.nova_igra(tezavnost)

        self.igre[uporabnisko_ime] = igra

        # self.igre.append(uporabnisko_ime[igra])

    def pridobi_igro(self, uporabnisko_ime):
        return self.igre[uporabnisko_ime]

class Igra():
    
    def __init__(self):
        self.trenutno_besedilo = ''
        self.zacetni_cas = ''
        self.koncni_cas = ''
        self.polje_povedi = []
        self.trenutni_indeks = 0
        self.st_napak = 0
        self.id_igre = ''
        self.tezavnost = ''

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
        for i in range(21):
            self.polje_povedi.append(random.choice(crke))
        self.trenutno_besedilo = self.polje_povedi[0]
    
    def pravilnost_besed(self,vneseno_besedilo):
        if self.trenutno_besedilo == vneseno_besedilo:
            self.koncni_cas = datetime.datetime.now()
            self.naslednje_besedilo()
            return True
        else: 
            self.st_napak += 1
            return False

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
        self.koncni_cas = ''
        self.st_napak = 0
        self.tezavnost = tezavnost
        
        if tezavnost == 'zelo lahko':
            self.izbor_random_crke()
        elif tezavnost == 'lahko':
            self.pripravi_besedilo('./besedila/besedilo-lahko.json')
        elif tezavnost == 'srednje':
            self.pripravi_besedilo('./besedila/besedilo-srednje.json')
        elif tezavnost == 'težko':
            self.pripravi_besedilo('./besedila/besedilo-tezko.json')

    def naslednje_besedilo(self):
        if self.trenutni_indeks < len(self.polje_povedi) - 1:
            self.trenutni_indeks += 1
            self.trenutno_besedilo = self.polje_povedi[self.trenutni_indeks]

    def konec_igre(self):
        if self.trenutni_indeks == len(self.polje_povedi) - 1:
            if self.koncni_cas == '':
                self.koncni_cas = datetime.datetime.now()
            return True
        else: return False

    def besede_na_minuto(self,cas):
        st_besed = 0
        seznam_besed = []
        for vrstica in self.polje_povedi:
            vrstica = vrstica.split(' ')
            for beseda in vrstica:
                seznam_besed.append(beseda)
        st_besed = len(seznam_besed)
        return int((st_besed / cas) * 60)

    def izpisi_rekord(self,vzdevek):
        if self.konec_igre:
            cas = round((self.koncni_cas - self.zacetni_cas).total_seconds(),2)
            wpm = self.besede_na_minuto(cas)
            st_napak = self.st_napak
            
            slovar = {"Ime": vzdevek, "ZaporednoMesto": 6, "Cas": cas, "St_napak": st_napak, "Wpm": wpm}
        return slovar

class Rekord():

    def __init__(self):
        self.rekordi_zelo_lahko = []
        self.rekordi_lahko = []
        self.rekordi_srednje = []
        self.rekordi_tezko = []

    def vrni_rekorde(self, tezavnost):
        if tezavnost == 'zelo lahko':
            return self.rekordi_zelo_lahko
        elif tezavnost == 'lahko':
            return self.rekordi_lahko
        elif tezavnost == 'srednje':
            return self.rekordi_srednje
        elif tezavnost == 'težko':
            return self.rekordi_tezko
        

    def preberi_rekorde(self):
        self.rekordi_zelo_lahko = []
        self.rekordi_lahko = []
        self.rekordi_srednje = []
        self.rekordi_tezko = []


        with open("rekordi.json") as f:
            seznam_rekordov = json.load(f)

            for tezavnost in seznam_rekordov:
                print(tezavnost)

                rekordi = []

                for rekord in tezavnost['rekordi']:
                    rekordi.append(rekord)

                rekordi.sort(key=lambda rekord: rekord['ZaporednoMesto'])

                for rekord in rekordi:
                    if tezavnost['tezavnost'] == 'zelo lahko':
                        self.rekordi_zelo_lahko.append(rekord)
                    elif tezavnost['tezavnost'] == 'lahko':
                        self.rekordi_lahko.append(rekord)
                    elif tezavnost['tezavnost'] == 'srednje':
                        self.rekordi_srednje.append(rekord)
                    elif tezavnost['tezavnost'] == 'tezko':
                        self.rekordi_tezko.append(rekord)

    def zapisi(self):
        zapis = [
                {
                "tezavnost": "zelo lahko",
                "rekordi": self.rekordi_zelo_lahko,
                },
                {
                "tezavnost": "lahko",
                "rekordi": self.rekordi_lahko,
                },
                {
                "tezavnost": "srednje",
                "rekordi": self.rekordi_srednje,
                },
                {
                "tezavnost": "tezko",
                "rekordi": self.rekordi_tezko,
                },
            ]

        with open('rekordi.json', 'w', encoding ='utf8') as f:
            json.dump(zapis, f)


    def razvrsti_rekorde(self,tezavnost,moj_rekord):
        self.preberi_rekorde()
        rekordi = []
        i_0 = 1
        if tezavnost == 'zelo lahko':
            rekordi = self.rekordi_zelo_lahko
        elif tezavnost == 'lahko':
            rekordi = self.rekordi_lahko
        elif tezavnost == 'srednje':
            rekordi = self.rekordi_srednje
        elif tezavnost == 'tezko':
            rekordi = self.rekordi_tezko
        rekordi.append(moj_rekord)

        rekordi.sort(key=lambda rekord: (rekord['Cas'], rekord['St_napak']))

        if len(rekordi) > 5:
            rekordi.pop()

        i = 1
        for rekord in rekordi:
            rekord['ZaporednoMesto'] = i
            i += 1


        if tezavnost == 'zelo lahko':
            self.rekordi_zelo_lahko = rekordi
        elif tezavnost == 'lahko':
            self.rekordi_lahko = rekordi
        elif tezavnost == 'srednje':
            self.rekordi_srednje = rekordi
        elif tezavnost == 'tezko':
            self.rekordi_tezko = rekordi
        self.zapisi()








            
            


    




    



