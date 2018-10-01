import socket as sock
import threading
import time
from builtins import print


stop = False


class Read (threading.Thread):

    def __init__(self, socketread):
        threading.Thread.__init__(self)
        self.s = socketread

    def run(self):
        while True:
            if not stop:
                string = self.s.recv(0xFF)
                print(string.decode("UTF-8"))
            else:
                return


def open_connection(address="localhost", port=10000):
    addr = (address, port)
    s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    s.connect(addr)
    return s


def send(server_socket, string="Hello"):
    if server_socket.sendall(bytes(string, encoding="UTF-8")) is None:
        print("Sended {}".format(string))
    else:
        print("Error, while sending string to server")


if __name__ == "__main__":
    try:
        socket = open_connection()
        reader = Read(socket)
        reader.start()
        
        send(socket, "Hello")
        time.sleep(2)
        send(socket, input("Some Data:"))
        send(socket, "stop")

        stop = True
        socket.close()
    except:
        print("Error while talking to server")