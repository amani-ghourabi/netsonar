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

    if network.prefixlen >= 31:
        total = network.num_addresses
    else:
        total = network.num_addresses - 2
    print("Usable hosts:", total)

    print("\nUsable IP addresses (first 10):")
    count = 0
    for address in network.hosts():
        if count == 10:
            break
        print(address)
        count = count + 1

    if total > 10:
        print(f"... and {total - 10} more")


ip = input("Enter your IPv4 address: ")
mask = input("Enter your subnet mask (e.g. 255.255.255.0 or /24): ").strip().lstrip("/")

network = get_network(ip, mask)
show_info(network)