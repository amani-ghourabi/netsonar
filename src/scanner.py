import ipaddress
import platform
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor


def is_host_alive(ip):
    if platform.system() == "Windows":
        command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(command, capture_output=True, text=True)
    return "TTL" in result.stdout.upper()


def scan_network(network):
    hosts = list(network.hosts())

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(is_host_alive, hosts))

    return [str(host) for host, alive in zip(hosts, results) if alive]


cidr = input("Enter the network to scan (e.g. 192.168.0.0/24): ").strip()

try:
    network = ipaddress.IPv4Network(cidr, strict=False)
except ValueError:
    print("Error: invalid network.")
    sys.exit(1)

if network.num_addresses > 256:
    print("Network too large. Use /24 or smaller.")
    sys.exit(1)

print(f"Scanning {network} ...")
online = scan_network(network)

print(f"\n{len(online)} device(s) online:")
for ip in online:
    print(ip)