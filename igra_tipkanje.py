import random

class Blok():
    def __init__(self,znak,barva):
        self.znak = znak
        self.barva = barva


def izbor_random_crke():
    crke = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    crka = random.choice(crke)
    return crka


crka = izbor_random_crke()
cas = 0
pravilno = 0
while cas < 60:
    vtipkana_crka = input('Vpisi črko').split().upper()
    if vtipkana_crka == crka:
        pravilno += 1
        continue
print(pravilno)
