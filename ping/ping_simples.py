import os

host = input("Digite o endereço host a ser verificado: ")

os.system(f'ping -n 6 {host}')