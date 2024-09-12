# server.py

import socket
import sys

def recursion(input):
    index = 0
    total = 0
    msg = [int(i) for i in str(input)]
    print(msg)
    for i in msg:
        print()
        print(total)
        total += i
        print(total)
        print()
    print('after for ' , total)
    new = [int(i) for i in str(total)]
    if(len(new) > 1):
        print('before recursion ' , total)
        recursion(total)
        return
    print('before return ', total)
    conn.sendall(str(total).encode())
    return total

'''while True:
    string = input()
    if string == '':
        break
    else: 
        print(str(recursion(string)))'''

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:  
                print('No data received. Closing Server')
                break
            else: 
                recursion(data)