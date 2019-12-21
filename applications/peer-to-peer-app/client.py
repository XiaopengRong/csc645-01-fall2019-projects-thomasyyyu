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
        self.client_host = '127.0.0.1'
        self.client_port = 12000
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
        self.client_host = ip_adress
        self.client_port = port
        try:
            self.client_socket.connect((self.client_host, self.client_port))
            client_id = self.receive(self.MEMORY_ALLOCATE_SIZE)
            self.client_id = int(client_id)
            print("Connected to server with ip address: " + self.client_host + " and port: " + str(self.client_port))
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


