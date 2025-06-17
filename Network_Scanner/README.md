# Network Scanner

this project is a simple network scanner designed fo rbeginners in cybersecurity. It allows users to scan a specified IP range to identify active hosts on the Network. The scanner utilizes Python libraries such as `socket` and `scapy` for efficient network interactions.

## Features

- Scan a specified IP range
- Check for active Hosts
- Report results in a user-friendly format

## Prerequistics

- Python 3.x installed on your machine.
- Required Python libraries listed in `requirements.txt`

## Installation

1. Clone the Repository:
```
git clone https://github.com/misbah-ullah01/network-scanner.git
```

2. Navigate to the project directory:
```
cd network-scanner
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

To use the network scanner, run the following command in your terminal:
```
python src/scanner.py <IP_RANGE>
```

Replace `<IP_RANGE>` with the desired range, for example, `192.168.1.0/24`

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggesstions or improvements.