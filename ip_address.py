import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        #print(f"The IP address of {domain} is: {ip_address}")
        return ip_address
    except socket.error as e:
        print(f"Unable to get IP address for {domain}: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain name of the web application (e.g., example.com): ")
    get_ip_address(domain)
