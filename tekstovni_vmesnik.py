from igra_tipkanje import Igra

igra = Igra()

def start(): 
    print('Pozdravljeni v igri Hitrostno tipkanje. Za začetek igre vpišite številko za izbrano težavnost.')
    print('1 - zelo lahko')
    print('2 - lahko')
    print('3 - srednje')
    print('4 - težko')

def izberi_tezavnost():
    tezavnost = input('Številka: ')
    if tezavnost == '1':
        return 'zelo lahko'
    elif tezavnost == '2':
        return 'lahko'
    elif tezavnost == '3':
        return 'srednje'
    elif tezavnost == '4':
        return 'težko'
    else:
        print('Neveljaven vnos')
        izberi_tezavnost()
    

def nova_igra():
    tezavnost = izberi_tezavnost()
    igra.nova_igra(tezavnost)
    while igra.trenutni_indeks != len(igra.polje_povedi) - 1:
        print(igra.trenutno_besedilo + " (" + str(igra.trenutni_indeks + 1) + "/" + str(len(igra.polje_povedi)-1) + ")")
        vnos = input('> ')
        if not igra.pravilnost_besed(vnos):
            print('Napačen vnos')
    konec()


def konec():
    print('Konec igre!')
    st_napak = igra.st_napak
    cas = round((igra.koncni_cas - igra.zacetni_cas).total_seconds(),2)
    wpm = igra.besede_na_minuto(cas)
    print('Čas: ' + str(cas))
    print('Število napak: ' + str(st_napak))
    print('Povprečno število napisanih besed na minuto (wpm): ' + str(wpm))
    
def nadaljevanje():
    print("Če hočete igro ponovno igrati vnesite DA, če hočete igro zaključiti vnesite NE")
    vnos = input('> ')
    if vnos.upper() == 'DA':
        tekstovni_vmesnik()
    else:
        print('Z igro ste zaljučili.')


def tekstovni_vmesnik():
    start()
    nova_igra()
    nadaljevanje()

#tekstovni_vmesnik()