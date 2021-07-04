import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("CLiente socket criado com sucesso")

host = 'localhost'
port = 5432

msg = 'Hello World'


try:
    print(f'Cliente: {msg}')
    s.sendto(msg.encode(),(host, port))

    dados, servidor = s.recvfrom(4096)

    dados = dados.decode()
    print(f'CLiente: {dados}')

except socket.error as e:
    print(e)

finally:
    print("CLiente fechando a conexao")
    s.close()