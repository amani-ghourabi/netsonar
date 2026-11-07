import platform
import subprocess


def is_host_alive(ip):
    if platform.system() == "Windows":
        command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(command, capture_output=True, text=True)
    return "TTL" in result.stdout.upper()


ip = input("Enter an IP address to check: ").strip()

if is_host_alive(ip):
    print(ip, "is online")
else:
    print(ip, "is offline")