# -*- coding: utf-8 -*-
""" The client
This file has the class client that implements a client socket.
Note that you can replace this client file by your client from
assignment #1.
"""
import socket
import pickle


class Client(object):
    def __init__(self):
        """
        TODO: implement this contructor
        Class contructor
        """
        self.host = None
        self.port = None
        self.client_id = None
        self.client_name = None
        self.newhost = None
        self.newport = None
        self.new_client_socket = None
        self.MEMORY_ALLOCATE_SIZE = 4096
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create here your client tcp socket

    def connect(self, ip_adress, port, client_name):
        """
        TODO: Implement connection to server sockets
        :param ip_adress:
        :param port:
        :return: VOID
        """
        self.host = ip_adress
        self.port = port
        try:
            self.client_socket.connect((self.host, self.port))
            client_id = self.receive(self.MEMORY_ALLOCATE_SIZE)
            self.client_id = int(client_id)
            print("Connected to server with ip address: " + self.host + " and port: " + str(self.port))
            print("Client id assigned by server is: " + str(self.client_id))
            self.client_name = client_name
            self.send(self.client_name)
            return True
        except socket.error as msg:
            print("Caught exception socket.error " + str(msg))
            self.close()
            return False

    def send(self, data):
        """
        TODO: Implement client socket send method
        :param data: raw_data. This data needs to be
                     serialized inside this method
                     with pickle before being sent.
                     You can also serialize objects
                     with pickle
        :return: VOID
        """
        serialized_data = pickle.dumps(data)
        self.client_socket.send(serialized_data)
        return 0

    def receive(self, memory_allocation_size):
        """
        TODO: implement receives data from server socket
        :param memory_allocation_size:
        :return: deserialized data
        """
        client_data = self.client_socket.recv(memory_allocation_size)
        deserialized_data = pickle.loads(client_data)
        return deserialized_data

    def close(self):
        """
        TODO: implement the close mechanish of a client socket
        :return: VOID
        """
        self.client_socket.close()
        return 0


"""
    def run(self):
        self.host = '127.0.0.1'
        self.port = 17865
        self.client_name = str(input("Enter the clientName: "))
        self.connect(self.host, self.port, self.client_name)
        while True:
            self.newhost = '127.0.0.1'
            self.newport = 12000
            self.new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.new_client_socket.bind((self.newhost, self.newport))
            self.new_client_socket.listen(100)
            while True:
                choose_d_u = input("What action are you tring to do? (Download/Upload): ")
                if choose_d_u == "Upload":
                    file_size = input("Please enter file size: ")
                    file_name = input("Please enter file name: ")
                    file_upload_speed = input("Please determine file upload speed: ")

                elif choose_d_u == "Download":
                    file_d_name = input("Please enter the file name that you want to download: ")
                    file_download_speed = input("Please determine file download speed: ")
                else:
                    print("please enter corrent info.")
                    break

client = Client()
client.run()
"""
