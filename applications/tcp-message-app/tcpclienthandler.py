import socket
import pickle
from time import time, ctime

#send_data = {None, None, None}


class TCPClientHandler(object):
    def __init__(self, client):
        self.client = client
        #self.printMenu()

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
        """
        option = int(input("Please select an option: "))
        if option == 1:
            self.getUserListFromServer()
        if option == 2:
            self.sendmessagetouser()
        if option == 3:
            self.getmessagefromserver()
        if option == 4:
            self.createnewchannel()
        if option == 5:
            self.p2pconnect()
        if option == 6:
            self.disconnectserver()
        """

    def getUserListFromServer(self, sock):
        #print("In 1")
        sock.send(pickle.dumps({'option': "1", 'userId': "None", 'msgs': "None"}))
        userList = sock.recv(4096)
        print(pickle.loads(userList))
        return 0

    def sendmessagetouser(self, sock):
        #sock.send(str.encode("2"))
        msg = input("Your message: ")
        otheruserId = input("userID recipent: ")
        listMsg = {'option': "2", 'userId': otheruserId, 'msgs': msg}
        sock.send(pickle.dumps(listMsg))
        print("Message sent!")
        return 0

    def getmessagefromserver(self, sock):
        #sock.send(str.encode("3"))
        getMsgs = {'option': "3", 'userId': "03090", 'msgs': "NotAMessage"}
        sock.send(pickle.dumps(getMsgs))
        msg = sock.recv(4096)
        print("Message:")
        #print(msg)
        print(pickle.loads(msg))
        print("in 3 test")
        return 0

    def createnewchannel(self, sock):
        sock.send(pickle.dumps({'option': "4", 'userId': "None", 'msg': "msg"}))
        host = input("Enter the ip address of the new channel: ")
        port = input("Enter the port to listen for new users: ")
        newServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = int(port)
        newServer.bind((host, port))
        newServer.listen()
        print("Waiting for users....")
        return 0
    def p2pconnect(self):
        return 0
    def disconnectserver(self):
        return 0