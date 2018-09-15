import socket

PORT = 1337

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', PORT))
serv_sock.listen(2)

while True:
    print("Start listen")

    client_sock0, client_addr1 = serv_sock.accept()
    print("I connect first player")
    client_sock0.sendall(b'0')

    client_sock1, client_addr2 = serv_sock.accept()
    print("I connect second player")
    client_sock1.sendall(b'1')

    player = 0

    while True:
        if not player:
            data = client_sock0.recv(1024)
            if not data:
                print("Player 1 RIP")
                client_sock1.sendall(b'Connection end')
                break
            client_sock1.sendall(data)
        else:
            data = client_sock1.recv(1024)
            if not data:
                print("Player 2 RIP")
                client_sock0.sendall(b'Connection end')
                break
            client_sock0.sendall(data)
        player += 1
        player %= 2

    client_sock0.close()
    client_sock1.close()