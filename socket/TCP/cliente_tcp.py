import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!!')
        print(f'Erro ==> {e}')
        sys.exit()

    print('Socket criado com sucesso!!!')

    host = input('Digite o host a ser conectado: ')
    port = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host,int(port)))
        print("CLiente TCP conectado com Sucesso!!")
        print(f'HOST: {host}')
        print(f'PORT: {port}')

        s.shutdown(2)
    except socket.error as e:
        print('Falha ao conectar o cliente TCP')
        print(f'Erro ==> {e}')
        sys.exit()


if __name__ == '__main__':
    main()