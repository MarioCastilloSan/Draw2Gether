import socket
from _thread import *
import sys

Server ="192.168.8.102"
port =5555

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((Server,port))
except socket.error as e:
    str(e)


s.listen(3)
print("Esperando por la conexion,el servidor ha sido iniciado")

def FHilo_Cliente(conn):
    reply=""
    while True:
        try:
            data=conn.recv(2048)
            reply=data.decode("utf-8")
            if not data:
                print("Desconectado")
                break
            else:
                print("Datos recividos: ",reply)
                print("Enviando: ",reply)
            conn.sendall(str.encode(reply))
        except:
            break

while True:
    conn,addr =s.accept()
    print("Conectado a :",addr)

    start_new_thread(FHilo_Cliente,(conn,))
