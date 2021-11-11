"""
Run this script, socket start listen 5000 port
Connect via telnet or nc (for example: telnet localhost 5000)
Get socket response (server socket response: Hello world)
If you try to connect using second telnet account
you can not get response from socket,
because it blocked by 1 client
"""

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

if __name__ == '__main__':
    while True:
        print('Before .accept()')
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)

        while True:
            print('Before .recv()')
            request = client_socket.recv(4096)

            if not request:
                break
            else:
                response = 'Hello world\n'.encode()
                client_socket.send(response)
