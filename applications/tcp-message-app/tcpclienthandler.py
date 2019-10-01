import socket
import pickle
from time import time, ctime


class TCPClientHandler(object):
    def __init__(self, client):
        self.client = client

    def printMenu(self):
        print("****** TCP Message App ******")
        print("-----------------------")
        print("Options Available: ")
        print("1. Get user list")
        print("2. Sent a message")
        print("3. Get my messages")
        print("4. Create a new channel")
        print("5. Chat in a channel with your friends")
        print("6. Diconnect from server")
        # above you need to implement all the menu

    def getUserListFromServer(self, sock):
        sock.send(pickle.dumps({'option': "1", 'userId': "None", 'msgs': "None"}))
        userList = sock.recv(4096)
        print(pickle.loads(userList))
        return 0

    def sendmessagetouser(self, sock):
        msg = input("Your message: ")
        otheruserId = input("userID recipent: ")
        listMsg = {'option': "2", 'userId': otheruserId, 'msgs': msg}
        sock.send(pickle.dumps(listMsg))
        print("Message sent!")
        return 0

    def getmessagefromserver(self, sock):
        getMsgs = {'option': "3", 'userId': "12345", 'msgs': "NotAMessage"}
        sock.send(pickle.dumps(getMsgs))
        msg = sock.recv(4096)
        print("My Message:")

        print(pickle.loads(msg))
        return 0

    def createnewchannel(self, sock, client_id, client_name, host, port):
        sock.send(pickle.dumps({'option': "4", 'userId': client_id, 'client_name': client_name}))
        while True:
            newServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = int(port)
            newServer.bind((host, port))
            newServer.listen(1)
            print("Waiting for users....")
            username = sock.recv(4096)
            message = newServer.recv(4096)
            if username:
                print("Userid:" + pickle.loads(username[0])+"connected to the channel")
                print("Enter bye to exit the channel")
            if message:
                print(pickle.loads(client_name) + ": " + pickle.loads(message))
            elif pickle.loads(message) is "bye":
                newServer.close()
    def p2pconnect(self, sock, client_id, client_name, new_socket):
        sock.send(pickle.dumps({'option': "5", 'userId': client_id, 'username': client_name}))
        message = input("please enter your message: ")
        new_socket.send(pickle.dumps(message))
    def disconnectserver(self, sock):
        return 0