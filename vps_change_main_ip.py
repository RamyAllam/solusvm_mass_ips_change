from vars import API_ID, API_KEY, API_URL
import requests


def change_main_ip(ipv4addr, vserverid):
    """
    :param ipv4addr: 
    :param vserverid: 
    :return:
    {'status': 'success', 'statusmsg': 'Main IP Address changed successfully'}
    {'status': 'error', 'statusmsg': 'IP not found'}
    """

    payload = {'action': 'vserver-mainip', 'id': API_ID, 'key': API_KEY, 'vserverid': vserverid,
               'ipv4addr': ipv4addr, 'rdtype': 'json'
               }
    r = requests.post(API_URL, data=payload)
    return r.json()
