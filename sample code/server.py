import socket

class Server(object):
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.sock.bind(('0.0.0.0',1234))

    def run(self):
        while True:
            (data,sender) = self.sock.recvfrom(1500)
            response = ' '.join(list(reversed(data.split())))
            self.sock.sendto(response, sender)

if __name__ == '__main__':
    s = Server(1234)
    s.run()
