import ipaddress

ip = '192.168.0.1'
ip_rede = ip + '/24'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip_rede, strict=False)

print(endereco + 256)
print(rede)

for ip_rede in rede:
    print(ip)