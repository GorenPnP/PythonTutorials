import socket as sock
from sys import exit


def open_server(address="localhost", port=10000):
    socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    server_address = (address, port)
    print("Starting Server at {} on port {}".format(server_address[0], server_address[1]))
    socket.bind(server_address)
    socket.listen(1)
    return socket


def close_server(socket):
    socket.close()


if __name__ == "__main__":
    s = open_server()
    while True:
        print("Waiting for connection")
        connection, client_address = s.accept()
        print("Incoming connection from {}".format(client_address[0]))
        while True:
            data = connection.recv(0xFF)

            if not data:
                break
            print ('received {}'.format(data.decode("UTF-8")))
            connection.sendall(data)
            if data.decode("UTF-8").__eq__("stop"):
                print("Closing server")
                close_server(s)

                exit(0)
                break


