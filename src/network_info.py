import ipaddress

ip = input("Enter your IPv4 address: ")
mask = input("Enter your subnet mask: ")

network = ipaddress.IPv4Network(
    f"{ip}/{mask}", strict=False
)

print("Network:", network.network_address)
print("Subnet:", network.netmask)
print("Broadcast:", network.broadcast_address)
print("Number of hosts:", network.num_addresses - 2)

print("\nUsable IP addresses:")

for address in network.hosts():
    print(address)