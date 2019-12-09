# -*- coding: utf-8 -*-
""" The server
This file has the class client that implements a server socket.
Note that you can replace this server file by your server from
assignment #1.
"""
import socket
import pickle
from _thread import *
import threading

global_array = {}


class Server(object):

    def __init__(self):
        """
        TODO: implement this constructor
        Class contructor
        """
        self.host = '127.0.0.1'
        self.port = 17865
        self.MAX_NUM_CONNECTIONS = 5
        self.client_id = None
        self.client_sock = None
        self.MAX_ALLOCATE_SIZE = 4096
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create here your client tcp socket

    def listen(self):
        """
        TODO: implement this method
        Listen for new connections
        :return: VOID
        """
        self.server_socket.listen(self.MAX_NUM_CONNECTIONS)
        return 0

    def accept(self):
        """
        TODO: implement this method
        Accept new clients
        :return:
        """
        client_sock, addr = self.server_socket.accept()
        self.client_id = addr[1]
        self.client_sock = client_sock
        return 0

    def recieve(self, memory_allocation_size):
        """
        TODO: implement this method
        Receives data from clients socket
        :param memory_allocation_size:
        :return: deserialized data
        """
        raw_data = self.client_sock.recv(memory_allocation_size)
        deserialized_data = pickle.loads(raw_data)
        return deserialized_data

    def sendData(self, data):
        """
        TODO: implement this method
        Implements send socket send method
        :param data: raw_data. This data needs to be
                     serialized inside this method
                     with pickle before being sent.
                     You can also serialize objects
                     with pickle
        :return: VOID
        """
        send_data = pickle.dumps(data)
        self.client_sock.sendall(send_data)
        return 0

    def threaded_client(self, conn, client_addr):
        """
        TODO: implement this method
        :param conn:
        :param client_addr:
        :return: a threaded client.
        """
        while True:
            data_from_client_string = conn.recv(4096)
            data_from_client = pickle.loads(data_from_client_string)
            if not data_from_client:
                print("Disconnect from server")
                break
        conn.close()
        return client_addr

    def run(self):
        print("Server Info")
        print("IP Address: " + self.host)
        print("port listening: " + str(self.port))
        print("waiting for connections...")
        self.server_socket.bind((self.host, self.port))
        self.listen()
        while True:
            try:
                self.accept()
                self.sendData(self.client_id)
                deserialized_data = self.recieve(self.MAX_ALLOCATE_SIZE)
                if self.client_id not in global_array:
                    global_array[self.client_id] = deserialized_data
                start_new_thread(self.threaded_client, (self.client_sock, self.client_id))
                print("Client: " + str(self.client_id) + " has connected to this server")
            except:
                print("Reach the maximum number of 5 people")
                break


server = Server()
server.run()
