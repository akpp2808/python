# -*- coding: utf-8 -*-
import pygeoip


GI = pygeoip.GeoIP('/usr/share/GeoIP/GeoIP.dat', pygeoip.MEMORY_CACHE)

print GI, dir(GI)
print GI.country_code_by_addr('46.227.139.202')

def get_country_name_by_addr(addr):
    try:
        return GI.country_name_by_addr(addr)
    except Exception:
        print('cannot get country by addr %s ' % addr)


def get_country_name_by_addrs(remote_addrs):
    '''
        @param remote_addrs: list of address
    '''
    if not remote_addrs:
        return None
    countries = []
    for addr in remote_addrs:
        country = get_country_name_by_addr(addr)
        if country:
            countries.append(country)

    return countries



IPS = ['',
       None,
       'default'
       '127.0.0.1',
       '216.107.154.139',
       '93.184.71.66',
       '71.60.164.106',
       '177.155.240.10',
       '198.23.143.79',
       '95.9.64.17',
       '80.93.49.145',
       '113.255.234.55',
       '199.168.138.241',
       '207.198.110.110',
       '112.78.139.130',
       '77.91.193.241',
       '121.22.127.17',
       '121.14.36.182',
       '177.43.192.129',
       '101.0.47.81',
       '142.0.79.222',
       '82.99.246.10',
       '89.203.137.193',
       '200.195.132.210',
       ]
addr = '127.0.0.1'
#for ip in IPS:
#    c = get_country_name_by_addr(ip)
#    print 'ip:%s|c:%s|' % (ip, c)

