#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process, Pool
import sys

#define address & buffer size
HOST = ""
PORT = 8002
BUFFER_SIZE = 1024

def main():
    proxy_host = '127.0.0.1'
    proxy_port = 8001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            proxy_socket, addr = s.accept()
            print("Connected by", addr)
            
            p = Process(target=echo_handler, args=(proxy_socket, addr))
            p.daemon = True
            p.start()

            # continue accepting data until no more left
            response_data = b""
            while True:
                data = proxy_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                response_data += data

                proxy_socket.sendall(response_data)


def echo_handler(proxy_socket, addr):        
    full_data = proxy_socket.recv(BUFFER_SIZE)
    time.sleep(0.5)
    proxy_socket.sendall(full_data)
    time.sleep(0.5)
    proxy_socket.shutdown(socket.SHUT_WR)

if __name__ == "__main__":
    main()
