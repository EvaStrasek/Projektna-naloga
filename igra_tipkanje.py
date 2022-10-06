import random
import time

class Blok():
    def __init__(self,znak,barva):
        self.znak = znak
        self.barva = barva


def izbor_random_crke():
    crke = 'ABCČDEFGHIJKLMNOPQRSŠTUVWXYZŽ'
    crka = random.choice(crke)
    return crka

def igra():
    crka = izbor_random_crke()
    cas = 0
    pravilno = 0
    while casovnik(90):
        vtipkana_crka = input('Vpisi črko').split().upper()
        if vtipkana_crka == crka:
           pravilno += 1
           crka = izbor_random_crke()
    print(pravilno)

def casovnik(cas = 90):
    while cas > 0:
        time.sleep(1)
        cas -= 1
    print('Čas se je iztekel. Igre je konec')


