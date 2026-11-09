import ipaddress
import platform
import subprocess
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


def scan_cidr(cidr):
    network = ipaddress.IPv4Network(cidr.strip(), strict=False)

    if not network.is_private:
        raise ValueError("Only private networks can be scanned.")
    if network.num_addresses > 256:
        raise ValueError("Network too large. Use /24 or smaller.")

    return scan_network(network)


if __name__ == "__main__":
    cidr = input("Enter the network to scan (e.g. 192.168.0.0/24): ")
    try:
        online = scan_cidr(cidr)
    except ValueError as error:
        print("Error:", error)
    else:
        print(f"\n{len(online)} device(s) online:")
        for ip in online:
            print(ip)