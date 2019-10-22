import socket
import pickle
import requests

class Client(object):
    """
    This class represents your client class that will send requests to the proxy server and will hand the responses to 
    the user to be rendered by the browser, 
    """

    def __init__(self):
        self.init_socket()
        self.client_socket = None

    def run(self, data):

        return 0

    def init_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return 0

    def _connect_to_server(self, host_ip, port):
        """
        Connects to server 
        remember to handle exceptions
        :param host_ip: 
        :param port: 
        :return: VOID
        """
        try:
            self.init_socket()
            self.client_socket.connect((host_ip, port))
            print("Socket successfully connected")
        except socket.error as err:
            print("socket connection failed with error %s" % err)
        return 0

    def _send(self, data):
        """
        1. Serialize data
        2. implements the primitive send() call from the socket
        :param data: {url: url, private_mode: True or false}
        :return: VOID
        """
        serialized_data = pickle.dumps(data)
        self.client_socket.send(serialized_data)
        return 0

    def _receive(self):
        """
        1. Implements the primitive rcv() method from socket
        2. Desirialize data after it is recieved
        :return: the desirialized data 
        """
        serialized_data = self.client_socket.recv(4096)
        data = pickle.loads(serialized_data)
        return data

    def request_to_proxy(self, data):
        """
        Create the request from data 
        request must have headers and can be GET or POST. depending on the option
        then send all the data with _send() method
        :param data: url and private mode 
        :return: VOID
        """
        
        return 0

    def response_from_proxy(self):
        """
        the response from the proxy after putting the _recieve method to listen.
        handle the response, and then render HTML in browser. 
        This method must be called from web_proxy_server.py which is the home page of the app
        :return: the response from the proxy server
        """
        return 0
