import mysql.connector
from vars import *


def get_vps_ips_count():
    """
    :return:
    List of dicts
    [{'vserverid': 0, 'count': 1994}, {'vserverid': 7, 'count': 2}, {'vserverid': 8, 'count': 2}]
    """
    vps_ips_date_list = []
    mydb = mysql.connector.connect(
      host=db_host,
      user=db_user,
      passwd=db_password,
      database=db_name
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT vserverid, COUNT(vserverid) FROM ipaddresses GROUP BY vserverid;")

    myresult = mycursor.fetchall()

    for x in myresult:
        vps_ips_date_dict = dict()
        vps_ips_date_dict['vserverid'] = x[0]
        vps_ips_date_dict['count'] = x[1]
        vps_ips_date_list.append(vps_ips_date_dict)
    return vps_ips_date_list


def get_vps_ips_list(vserverid):
    """
    :param vserverid:
    :return: List of IPs for this specific server
    """
    vps_ips_list = []
    mydb = mysql.connector.connect(
      host=db_host,
      user=db_user,
      passwd=db_password,
      database=db_name
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT ipaddress FROM ipaddresses where vserverid='{}'".format(vserverid)
    )

    myresult = mycursor.fetchall()

    for x in myresult:
        vps_ips_list.append(x[0])
    return vps_ips_list
