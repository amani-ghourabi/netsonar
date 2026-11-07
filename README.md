# IPv4 Network Information Tool

A simple Python project that analyzes an IPv4 address and its subnet mask to calculate essential network information.

## Features

- Accepts an IPv4 address and a subnet mask (`255.255.255.0`, `/24` or `24`).
- Validates input and shows a clear error message.
- Calculates the network address and broadcast address.
- Displays the number of usable hosts.
- Lists the first 10 usable IP addresses (and how many more exist).
- Handles `/31` and `/32` networks correctly.

## Technologies Used

- **Language:** Python 3
- **Module:** `ipaddress` (Python standard library)

## Project Structure

```text
technical-projects/
├── .gitignore
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

On Linux/macOS, use `python3 src/network_info.py` instead.

## Example

**Input:**

```text
Enter your IPv4 address: 192.168.1.10
Enter your subnet mask (e.g. 255.255.255.0 or /24): 255.255.255.0
```

**Output:**

```text
Network: 192.168.1.0
Subnet mask: 255.255.255.0
Broadcast: 192.168.1.255
Usable hosts: 254

Usable IP addresses (first 10):
192.168.1.1
192.168.1.2
...
192.168.1.10
... and 244 more
```
**Invalid input:**

```text
Enter your IPv4 address: 192.168.1.1.10
Enter your subnet mask (e.g. 255.255.255.0 or /24): /24
Error: invalid IP address or subnet mask.
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