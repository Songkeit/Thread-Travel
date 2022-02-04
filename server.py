import socket

def server():
    host_ip = socket.gethostbyname(socket.gethostname())
    port = 5000
    buffer = []

    name_seat = {}

    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.bind((host_ip, port))
        server.listen(1)

        print("wait")
        client, addr = server.accept()
        print("connect", str(addr))

        data = client.recv(1024).decode('utf-8')
        try:
            data = str(data)
            data = data.split(',')

            if data[1] in buffer:
                client.send(data[1].encode('utf-8'))
            else:
                buffer.append(data[1])
                name_seat[data[0]] = data[1]
                respones = 'success'
                client.send(respones.encode('utf-8'))
        except:
            pass

        print(buffer)
        print(name_seat)
        
        client.close()
    
