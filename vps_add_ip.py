from vars import API_ID, API_KEY, API_URL
import requests


def add_ip(ipv4addr, vserverid):
    """
    :param ipv4addr: 
    :param vserverid: 
    :return:
    {'status': 'success', 'statusmsg': 'IP address added', 'ipaddress': '50.3.200.2'}
    {'status': 'error', 'statusmsg': 'IP not found'}
    """

    payload = {'action': 'vserver-addip', 'id': API_ID, 'key': API_KEY, 'vserverid': vserverid,
               'ipv4addr': ipv4addr, 'rdtype': 'json'
               }
    r = requests.post(API_URL, data=payload)
    return r.json()
