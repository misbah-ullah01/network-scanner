import socket
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    active_hosts = []
    try:
        # Create an ARP request to find active hosts in the specified IP range
        arp_request = ARP(pdst=ip_range)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        for element in answered_list:
            active_hosts.append(element[1].psrc)
    except Exception as e:
        print(f"An error occured: {e}")

    return active_hosts

def main():
    ip_range = input("Enter the IP range to scan (e.g. 192.168.1.1/24): ")
    print(f"Scanning {ip_range}...")
    active_hosts = scan_network(ip_range)

    if active_hosts:
        print("Active hosts found: ")
        for host in active_hosts:
            print(host)
    else:
        print("No active hosts found.")

if __name__ == "__main__":
    main()