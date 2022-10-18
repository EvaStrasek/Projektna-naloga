import bottle
from igra_tipkanje import Igra,Tipkanje

igra_tipkanje = Tipkanje()

@bottle.get('/')
def zacetna_stran():
    tezavnosti = ["zelo lahko","lahko","srednje","težko"]
    return bottle.template('zacetna_stran.tpl',tezavnosti = tezavnosti)

@bottle.post('/nova_igra')
def nova_igra():
    tezavnost = bottle.request.forms.getunicode('tezavnost')
    if tezavnost == "zelo lahko":
        #"izbira_random_crke * 20"
        pass
    elif tezavnost == "lahko":
        # besedilo3.json
        pass
    elif tezavnost == "srednje":
        # besedilo2.json
        pass
    elif tezavnost == "težko":
        # besedilo1.json
        pass


bottle.run(debug = True,reload = True)


