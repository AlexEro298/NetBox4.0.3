import time
import pynetbox
import urllib3
from ping3 import ping

netbox_url = ''
netbox_api = ''
nb = pynetbox.api(url=netbox_url, token=netbox_api)
# Disable SSL and SSL Warnings
nb.http_session.verify = False
urllib3.disable_warnings()


ip_all = nb.ipam.ip_addresses.all()
edit_ip = []
edit_ip_new_status = []

for ip in ip_all:
    time.sleep(1)
    print(ip)
    id_ip = ip.id
    status_value = str(list(ip.status)[0]).replace('\'','').replace('(','').replace(')','').replace(' ','').split(',')[1]
    result_ping = ping(str(ip.display).split('/')[0])
    if result_ping != False:
        if result_ping != None:
            new_status_value = 'active'
        else:
            new_status_value = 'deprecated'
    else:
        new_status_value = 'deprecated'

    if (status_value == new_status_value) and (status_value!='reserved'):
        print('Все Ок')
    else:
        nb.ipam.ip_addresses.all().update(id = ip.id, status = new_status_value)
        edit_ip.append(ip.display)
        edit_ip_new_status.append(new_status_value)
print(edit_ip)
print(edit_ip_new_status)




