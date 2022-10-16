import bottle
from igra_tipkanje import Igra

@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.tpl')

bottle.run(debug = True,reload = True)


