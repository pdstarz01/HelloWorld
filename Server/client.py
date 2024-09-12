#client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = str(input("What would you like to send to the server?: "))
        s.sendall(msg.encode('utf-8'))
        if msg == '':
            print('No data detected. Closing Connection')
            break
        data = s.recv(1024).decode('utf-8')
        print(f"Received {data!r}")