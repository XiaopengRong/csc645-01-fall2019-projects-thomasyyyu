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
        #print("ListMsg is:" + listMsg)
        msgs = ':'.join(listMsg)
        sock.send(pickle.dumps(msgs))
        print("Message sent!")
        return 0

    def getmessagefromserver(self, sock):
        #sock.send(str.encode("3"))
        getMsgs = {'option': "3", 'client_id': "03090", 'msgs': "NotAMessage"}
        msgs = ':'.join(getMsgs)
        print(msgs)
        sock.send(str.encode(msgs))
        print("before msg")
        msg = sock.recv(4096)
        print("Message:")
        print(msg)
        return 0

    def createnewchannel(self):
        return 0
    def p2pconnect(self):
        return 0
    def disconnectserver(self):

        return 0