import socket

HOST = "127.0.0.1"
PORT = 60001

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 60001))
serv_sock.listen(2)

while True:
    print("Start listen")

    client_sock1, client_addr1 = serv_sock.accept()
    print("I connect first player")
    client_sock1.sendall(b'0')

    client_sock2, client_addr2 = serv_sock.accept()
    print("I connect second player")
    client_sock2.sendall(b'1')

    client_sock1.close()
    client_sock2.close()