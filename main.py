from vps_add_ip import add_ip
from vps_delete_ip import delete_ip
from vps_change_main_ip import change_main_ip
from get_vps_ips import get_vps_ips_list, get_vps_ips_count
from vars import ips_pool, vserverid_exclude_list


# GET number of IPs per VPS
"""
Returns: {'vserverid': 2036, 'count': 6}
"""
for i in get_vps_ips_count():
    vserverid = i['vserverid']
    count = i['count']

    # Exclude the servers in the exclude list
    if vserverid not in vserverid_exclude_list:
        # GET Current Assigned IPs
        # Returns a list of IPs
        current_assigned_ips_list = get_vps_ips_list(vserverid)

        print("VPS: {} has {} of IPs".format(vserverid, count))

        # Add New IP
        new_ips_added = []
        for ip in range(count):
            new_ip_from_pool = ips_pool[0]
            new_ips_added.append(new_ip_from_pool)
            print("Adding {}".format(new_ip_from_pool))

            print(add_ip(new_ip_from_pool, vserverid))

            # Remove the new assigned IP from the available pool
            ips_pool.remove(new_ip_from_pool)

        # Change the main IP
        main_ip = new_ips_added[0]
        print("Changing the main IP to {}".format(main_ip))
        print(change_main_ip(main_ip, vserverid))

        # Removing old assigned IPs
        for ip in current_assigned_ips_list:
            print("Removing {} From VPS: {}".format(ip, vserverid))
            print(delete_ip(ip, vserverid))

        print("==============================")
