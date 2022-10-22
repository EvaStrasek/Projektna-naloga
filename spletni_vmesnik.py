import bottle
from igra_tipkanje import Igra

igra_tipkanje = Igra()

@bottle.get('/')
def zacetna_stran():
    tezavnosti = ["zelo lahko","lahko","srednje","težko"]
    return bottle.template('zacetna_stran.tpl',tezavnosti = tezavnosti)

@bottle.post('/nova-igra')
def nova_igra():
    tezavnost = bottle.request.forms.getunicode('tezavnost')
    igra_tipkanje.nova_igra(tezavnost)

    bottle.redirect('/igra')

@bottle.get('/igra')
def igra():
    trenutno_besedilo = igra_tipkanje.trenutno_besedilo


    return bottle.template('igra.tpl', trenutno_besedilo = trenutno_besedilo)

@bottle.post('/preveri-besedilo')
def preveri_besedilo():
    besedilo = bottle.request.forms.getunicode('besedilo')
    igra_tipkanje.pravilnost_besed(besedilo)
    bottle.redirect('/igra')

@bottle.post('/konec-igre')
def konec_igre():
    igra_tipkanje.konec_igre(igra_tipkanje.self)
    cas = igra_tipkanje.koncni_cas - igra_tipkanje.zacetni_cas
    wpm = igra_tipkanje.besede_na_minuto(cas)
    return bottle.template('koncna_stran.tpl')






bottle.run(debug = True,reload = True)


