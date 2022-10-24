import bottle
from igra_tipkanje import Igra, Stanje

SIFRIRNI_KLJUC = 'toJeSifrirniKljuc'

stanje_iger = Stanje()

def stanje_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)

    if uporabnisko_ime == None:
        bottle.redirect('/')
    else:
        return stanje_iger.pridobi_igro(uporabnisko_ime)

@bottle.get('/')
def zacetna_stran():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)

    tezavnosti = ["zelo lahko", "lahko", "srednje", "težko"]
    return bottle.template('zacetna_stran.tpl',tezavnosti = tezavnosti, uporabnisko_ime = uporabnisko_ime)


@bottle.post('/nova-igra')
def nova_igra():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    tezavnost = bottle.request.forms.getunicode('tezavnost')
    
    stanje_iger.nova_igra(uporabnisko_ime, tezavnost)

    # igra_tipkanje.nova_igra(tezavnost)

    bottle.response.set_cookie('uporabnisko_ime', uporabnisko_ime, path='/', secret=SIFRIRNI_KLJUC)

    bottle.redirect('/igra')

@bottle.get('/igra')
def igra():
    # uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    
    # stanje_iger.pridobi_igro(uporabnisko_ime)

    igra_tipkanje = stanje_uporabnika()

    if igra_tipkanje.konec_igre():
        bottle.redirect('/konec-igre')

    trenutno_besedilo = igra_tipkanje.trenutno_besedilo
    trenutni_indeks = igra_tipkanje.trenutni_indeks + 1
    st_indeksov = len(igra_tipkanje.polje_povedi) - 1

    return bottle.template('igra.tpl', trenutno_besedilo = trenutno_besedilo,trenutni_indeks = trenutni_indeks, st_indeksov= st_indeksov)

@bottle.post('/preveri-besedilo')
def preveri_besedilo():
    besedilo = bottle.request.forms.getunicode('besedilo')

    igra_tipkanje = stanje_uporabnika()

    igra_tipkanje.pravilnost_besed(besedilo)
    bottle.redirect('/igra')

@bottle.get('/konec-igre')
def konec_igre():
    igra_tipkanje = stanje_uporabnika()

    if igra_tipkanje.konec_igre():
        st_napak = igra_tipkanje.st_napak
        cas = round((igra_tipkanje.koncni_cas - igra_tipkanje.zacetni_cas).total_seconds(),2)
        wpm = igra_tipkanje.besede_na_minuto(cas)
        return bottle.template('koncna_stran.tpl', st_napak = st_napak, cas = cas, wpm = wpm)
    else: bottle.redirect('/igra')

@bottle.get("/img/<slika>")
def pokazi_sliko(slika):
    return bottle.static_file(slika, root="img")






bottle.run(debug = True,reload = True)


