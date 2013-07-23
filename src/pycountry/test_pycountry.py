import pycountry
#http://ru.wikipedia.org/wiki/ISO_3166-1
#http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#http://www.loc.gov/standards/iso639-2/php/English_list.php
#http://www.loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt


#print dir(pycountry.countries)
#ua = pycountry.countries.get(alpha2='EU')
#print ua

for c in pycountry.countries:
    print c.name, c.alpha2
    pass


#print dir(pycountry.Languages.data_class_base)
#'data_class_base', 'data_class_name', 'field_map', 'get', 'no_index', 'xml_tag'


langs = []
max = 2
for l in pycountry.languages:
    if hasattr(l, 'alpha2'):
        if len(l.name) > max:
            max = len(l.name)
#            print len(l.name), max, l.name 
#        langs.append(l)
#        if not l.alpha2 == 'ga':
#            continue
#        print l.alpha2, l.name

