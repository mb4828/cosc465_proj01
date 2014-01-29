import socket

class Client(object):
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        data = raw_input("What message to send? ")
        self.sock.sendto(data, (self.server, self.port) )
        (data, serveraddr) = self.sock.recvfrom(1500)
        print "Received from {}:{}> {}".format(serveraddr[0], serveraddr[1], data)
        self.sock.close()

if __name__ == '__main__':
    c = Client('127.0.0.1', 1234)
    c.run()
