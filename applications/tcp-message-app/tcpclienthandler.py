import socket
import pickle
from _thread import *
import threading
from time import time, ctime

user_name_msg = {}
user_name_msg1 = {}

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

    def sendmessagetouser(self, sock, date, clientName):
        msg = input("Your message: ")
        otheruserId = input("userID recipent: ")
        msg += (" " + "  (from: "+clientName+")" + str(date) )
        listMsg = {'option': "2", 'userId': otheruserId, 'msgs': msg}
        #print(listMsg)
        sock.send(pickle.dumps(listMsg))
        print("Message sent!")
        return 0

    def getmessagefromserver(self, sock):
        getMsgs = {'option': "3", 'userId': "12345", 'msgs': "NotAMessage"}
        sock.send(pickle.dumps(getMsgs))
        msg = sock.recv(4096)
        print("My Message:")
        myMsgs = pickle.loads(msg)
        print(*myMsgs, sep="\n")
        return 0

    def createnewchannel(self, socket, host, port, client_name, user_name):
        #socket.listen(100)
        print("Channel Info:")
        print("IP Address: " + host)
        print("Channel Clientid:" + str(port))
        print("Waiting for users....")
        client_sock, addr = socket.accept()
        print("UserId " + str(addr[1])+"connected to the channel")
        print("Enter Bye to exit the channel")
        #client_sock.connect((host, port))
        while True:
            try:
                userMeg = client_sock.recv(4096)
                userMeg_decode = pickle.loads(userMeg)
                for x, y in userMeg_decode.items():
                    print(x+": " + y)
                user_input = input(str(client_name) + ": ")
                user_input = str(user_input)
                user_name_msg[client_name] = user_input
                if "bye" in user_input:
                    print("You have disconnect server")
                    break
                user_encode = pickle.dumps(user_name_msg)
                client_sock.send(user_encode)
            except:
                print("Client Disconnected!")
                break

    def p2pconnect(self, client_name, user_name):
        connectHost = input("Enter the ip address of the channel you would like to connect:")
        connectPort = input("Enter the channel port: ")
        connectPort = int(connectPort)
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((connectHost, connectPort))
        print("Successfully connected to the channel " + str(connectPort))
        print("Enter 'Bye' to close the chat.")
        while True:
            try:
                client_in = input(str(client_name) + ": ")
                client_in = str(client_in)
                user_name_msg1[client_name] = client_in
                if "bye" in client_in:
                    print("You have disconnect server")
                    break
                client_encode = pickle.dumps(user_name_msg1)
                client_sock.send(client_encode)
                client_income_message = client_sock.recv(4096)
                client_income_message_decode = pickle.loads(client_income_message)
                if "bye" in client_income_message_decode:
                    print("Other user disconnect channel")
                    break
                for x, y in client_income_message_decode.items():
                    print(x+": " + y)
            except:
                print("Other user exit channel")
                break

    def disconnectserver(self, sock, new_sock):
        return 0