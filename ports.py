import socket

# Common ports list for a fast scan
COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 8080,8064
]

def scan_ports(target):
   
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Starting fast scan on target: {target_ip}")
        for port in COMMON_PORTS:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set timeout to avoid hanging
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
        print("Fast scan finished.")
    except KeyboardInterrupt:
        print("\nScan interrupted by the user.")
    except socket.error as err:
        print(f"Socket error: {err}")

if __name__ == "__main__":
    target = input("Enter the target to scan (IP or hostname): ")
    scan_ports(target)