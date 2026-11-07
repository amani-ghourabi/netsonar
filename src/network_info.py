import ipaddress
import sys


def get_network(ip, mask):
    try:
        return ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    except ValueError:
        print("Error: invalid IP address or subnet mask.")
        sys.exit(1)


def show_info(network):
    print("Network:", network.network_address)
    print("Subnet mask:", network.netmask)
    print("Broadcast:", network.broadcast_address)
    print("Usable hosts:", network.num_addresses - 2)

    print("\nUsable IP addresses:")
    for address in network.hosts():
        print(address)


ip = input("Enter your IPv4 address: ")
mask = input("Enter your subnet mask: ")

network = get_network(ip, mask)
show_info(network)