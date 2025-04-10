from ports import scan_ports
from ip_address import get_ip_address
from filecheck import main

print("*"*70)
print("wellcome to tool kit")
print("*"*70)
print("")
print("1.ports scanner")
print("")
print("2.file integrity checker")
print("")

opstion = int(input("enter the operation number:"))

if opstion==1:
    domain=input('enter the domain name')
    ip=get_ip_address(domain)
    scan_ports(str(ip))
elif opstion==2:
    main()
else:
    print("enter the valid number")