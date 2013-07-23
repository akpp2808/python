from iso3166 import countries
import iso3166
#print dir(iso3166)


for c in countries:
    if c.alpha2 == 'EU':
        print c, c.name, c.alpha2, c.alpha3, c.numeric