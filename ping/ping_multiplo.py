import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f'Host: {ip}')
        os.system(f'ping -n 2 {ip}')
        time.sleep(2)