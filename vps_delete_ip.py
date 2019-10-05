from vars import API_ID, API_KEY, API_URL
import requests


def delete_ip(ipaddr, vserverid):
    """
    :param ipaddr:
    :param vserverid:
    :return:
    {'status': 'success', 'statusmsg': 'Ip address removed'}
    {'status': 'error', 'statusmsg': 'Ip address not found'}
    """
    payload = {'action': 'vserver-delip', 'id': API_ID, 'key': API_KEY, 'vserverid': vserverid,
               'ipaddr': ipaddr, 'rdtype': 'json'
               }
    r = requests.post(API_URL, data=payload)
    return r.json()
