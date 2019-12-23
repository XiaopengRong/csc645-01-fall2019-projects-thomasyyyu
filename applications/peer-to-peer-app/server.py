# -*- coding: utf-8 -*-
""" The server
This file has the class client that implements a server socket.
Note that you can replace this server file by your server from
assignment #1.
"""
import socket
import pickle


class Server(object):

    def __init__(self):
        self.global_dic = {}
        self.MAX_NUM_CONNECTIONS = 5
        self.client_id = None
        self.client_sock = None
        self.MAX_ALLOCATE_SIZE = 4096
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create here your client tcp socket

    def listen(self):
        self.server_socket.listen(self.MAX_NUM_CONNECTIONS)
        return 0

    def accept(self):
        client_sock, addr = self.server_socket.accept()
        self.client_id = addr[1]
        self.client_sock = client_sock
        return 0

    def recieve(self, memory_allocation_size):
        raw_data = self.client_sock.recv(memory_allocation_size)
        deserialized_data = pickle.loads(raw_data)
        return deserialized_data

    def sendData(self, data):
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
        return data_from_client

