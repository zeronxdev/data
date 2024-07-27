from colorama import Fore
import requests

def get_location(ip_addr):
    ip_address = ip_addr
    response = requests.get(f'https://ipinfo.io/{ip_address}/json?token=48b92fc0bdea95').json()
    asn = response['asn']['asn']
    asnname = response['asn']['name']
    company_name = response['company']['name']
    company_domain = response['company']['domain']
    city = response['city']
    region_city = response['region']
    country = response['country']
    timezone = response['timezone']

    location_data = f'''
IPv4            : {ip_address}
# ASN  
  ASN             : {asn}
  ASN Name        : {asnname}
# Company  
  Company Name    : {company_name}
  Company Domain  : {company_domain}
# Location  
  City            : {city}
  Region          : {region}
  Country         : {country}
# TIME
  Timezone        : {timezone}
'''

    return location_data

def ip_to_loc(args, send, client, gray):
    try:
        ip = ''
        if len(args) == 2:
            ip = str(args[1])
            ip_location = get_location(ip)
            for x in ip_location.split('\n'):
                send(client, f'{gray}' + x)
        else:
            send(client, Fore.LIGHTWHITE_EX + '\n!GEOIP [IP]\n')
    except:
        send(client, Fore.RED + '\nInvalid data\n')