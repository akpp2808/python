#http://rutracker.org/forum/viewtopic.php?t=3921625
#http://www.famfamfam.com/lab/icons/flags/
import pygeoip
import os

#COUNTRY_DB_PATH = '/usr/share/GeoIP/GeoIP.dat'
#COUNTRY_DB_PATH = '/usr/share/GeoIP/GeoIPv6.dat'
CITY_DB_PATH = '/usr/share/GeoIP/GeoIPCity.dat'
COUNTRY_DB_PATH = '/usr/share/GeoIP/GeoLiteCity.dat'



#GI = pygeoip.GeoIP(COUNTRY_DB_PATH, pygeoip.MEMORY_CACHE)
GI = pygeoip.GeoIP(COUNTRY_DB_PATH)
#GIC = pygeoip.GeoIP(CITY_DB_PATH)
ip = '109.108.247.177'
#ip = '64.233.161.99'
ip = '2.135.31.151'

print GI.country_name_by_addr(ip)
#print GIC.region_by_addr(ip)
#print GIC.record_by_addr(ip)
#print dir(GIC)

