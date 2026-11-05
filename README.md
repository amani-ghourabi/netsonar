# IPv4 Network Information Tool

A simple Python project that analyzes an IPv4 address and its subnet mask to calculate essential network information.

## Features

- Accepts an IPv4 address and subnet mask.
- Calculates the network address.
- Identifies the subnet mask.
- Calculates the broadcast address.
- Displays the number of usable host addresses.
- Lists all usable IP addresses.

## Technologies Used

- **Language:** Python 3
- **Module:** `ipaddress` (Python standard library)

## Project Structure

```text
python-network-scanner/
│
├── README.md
└── src/
    └── network_info.py
```

## Requirements

- Python 3.x
- No external libraries required.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/amani-ghourabi/technical-projects.git
```

2. Navigate to the project directory:

```bash
cd technical-projects
```

3. Run the Python script:

```bash
python src/network_info.py
```

## Example

**Input:**

```text
Enter your IPv4 address: 192.168.1.10
Enter your subnet mask: 255.255.255.0
```

**Output:**

```text
Network: 192.168.1.0
Subnet: 255.255.255.0
Broadcast: 192.168.1.255
Number of hosts: 254

Usable IP addresses:
192.168.1.1
192.168.1.2
...
192.168.1.254
```

## Learning Objectives

This project was developed to practice:

- IPv4 addressing
- Subnet masks
- Network and broadcast addresses
- Usable host addresses
- Python programming
- Network fundamentals

## Author

**Amani Ghourabi**

GitHub: [amani-ghourabi](https://github.com/amani-ghourabi)