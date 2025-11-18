#  this program pings a range of IPs
from scapy.all import *


def myping(ip):
    #  creating an ICMP echo request type packet with type=8 and code = 0 (default values)
    icmp_pkt = IP(dst=ip) / ICMP()

    #  sending and receiving ICMP pkts to/from the target device
    response_pkt = sr1(icmp_pkt, timeout=3, verbose=0)

    #  displaying response
    if response_pkt:
        if response_pkt.getlayer('ICMP').type == 0:
            print(f'{ip} is reachable')
        else:
            print(f'{ip} is not reachable')  # in the case of a firewall blocking pings
    else:
        print(f'{ip} is not reachable')  # this ip is not in use or not connected to the network


def main():
    target_ip_prefix = '10.52.80.' #  select octets to match network
    for last_octet in range(1, 255): #  range: 10.52.80.1 - 10.52.80.254
        target_ip = target_ip_prefix + str(last_octet)
        myping(target_ip)


main()
