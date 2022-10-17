import bottle
from igra_tipkanje import Igra

@bottle.get('/')
def zacetna_stran():
    tezavnosti = ["lahko","srednje","težko"]
    return bottle.template('zacetna_stran.tpl',tezavnosti = tezavnosti)

bottle.run(debug = True,reload = True)


