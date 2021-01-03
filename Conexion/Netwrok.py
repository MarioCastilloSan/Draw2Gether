import socket

class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.Server="192.168.8.102"
        self.port=5555
        self.addr=(self.Server,self.port)
        self.id=self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
n=Network()
print(n.send('Prueba 1'))
print(n.send('Prueba 2'))
print(n.send('Prueba 3'))