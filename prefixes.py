import pynetbox
import urllib3
from ping3 import ping

netbox_url = 'https://10.10.13.75/'
netbox_api = '0829d3d7ced67e2bb6eba56305d61a2925a19d61'
nb = pynetbox.api(url=netbox_url, token=netbox_api)
# Disable SSL and SSL Warnings
nb.http_session.verify = False
urllib3.disable_warnings()


#Receive prefixes
ip_prefixes_all = nb.ipam.prefixes.all()
ip_prefixes_management = []
ip_prefixes_access_networks= []
ip_prefixes_real_network = []
ip_prefixes_loopback = []

for ip_prefix in ip_prefixes_all:
    for tags in ip_prefix.tags:
        if tags.name == 'Access Networks':
            ip_prefixes_access_networks.append(ip_prefix)
        elif tags.name == 'Management':
            ip_prefixes_management.append(ip_prefix)
        elif tags.name == 'Real Network':
            ip_prefixes_real_network.append(ip_prefix)
        elif tags.name == 'Loopback':
            ip_prefixes_loopback.append(ip_prefix)
        else:
            print('Такого тэга нет')

print(ip_prefixes_loopback)
print(ip_prefixes_real_network)
print(ip_prefixes_management)
print(ip_prefixes_access_networks)