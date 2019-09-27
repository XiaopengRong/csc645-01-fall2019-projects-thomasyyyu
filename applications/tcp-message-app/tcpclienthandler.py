import socket
import pickle


class Client(object):
    def __init__(self, host, port, cName):
        self.host = host
        self.port = port
        self.cName = cName


user = Client('127.0.0.1', int(17865), None)

myPort = user.port
myHost = user.host
clientName = user.cName

try:
    myHost = input("Enter the server IP Address: ")
    myPort = input("Enter the server port: ")
    clientName = input("Your id key (i.e your name): ")
except:
    print("Error")
