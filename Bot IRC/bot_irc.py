import socket


def envia_comando(sock, comando):
    comando += '\r\n'
    sock.send(comando.encode('UTF-8'))

def registra(sock, nick):
    envia_comando(sock, 'NICK {}'.format(nick))
    envia_comando(sock, 'USER {0} {0} {0} :{0}'.format(nick))

def checa_ping(sock, msg):
    if 'PING :' in msg:
        codigo_ping = msg.split('PING :')[-1]
        resposta_pong = 'PONG :{}'.format(codigo_ping)
        envia_comando(sock, resposta_pong)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('irc.rizon.net', 6667))

dados = s.recv(2048)
print(dados)

msg = s.recv(2048).decode('UTF-8')
print(msg)

nick = 'Ella Darte'
comando_nick = f'NICK {nick}\r\n'.encode('UTF-8')
s.send(comando_nick)

comando_user = f'USER {nick} {nick} {nick} :{nick}\r\n'.encode('UTF-8')
s.send(comando_user)

registra(s, 'BotDaEmpresa')

while True:
    msg = s.recv(2048).decode('UTF-8')
    print(msg)

    
    if 'PING :' in msg:
        codigo_ping = msg.split('PING :')[-1]
        resposta_pong = 'PONG :{}'.format(codigo_ping)
        envia_comando(s, resposta_pong)

    while True:
        msg = s.recv(2048).decode('UTF-8')
        print(msg)
        checa_ping(s, msg)