import socket
import pickle


class Client(object):
    """
    This class represents your client class that will send requests to the proxy server and will hand the responses to 
    the user to be rendered by the browser, 
    """

    def __init__(self):
        self.client_socket = None
        self.proxy_msg = None

    def init_socket(self, data):
        host = '127.0.0.1'
        port = 17865
        self._connect_to_server(host, port, data)

    def _connect_to_server(self, host_ip, port, data):
        """
        Connects to server 
        remember to handle exceptions
        :param host_ip:
        :param port:
        :return: VOID
        """
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((host_ip, port))
            self.request_to_proxy(data)
        except socket.error as err:
            print("socket connection failed with error %s" % err)

    def _send(self, data):
        """
        1. Serialize data
        2. implements the primitive send() call from the socket
        :param data: {url: url, private_mode: True or false}
        :return: VOID
        """
        serialized_data = pickle.dumps(data)
        self.client_socket.send(serialized_data)

    def _receive(self):
        """
        1. Implements the primitive rcv() method from socket
        2. Desirialize data after it is recieved
        :return: the desirialized data 
        """
        serialized_data = self.client_socket.recv(4096)
        deserialized_data = pickle.loads(serialized_data)
        return deserialized_data

    def request_to_proxy(self, data):
        """
        Create the request from data 
        request must have headers and can be GET or POST. depending on the option
        then send all the data with _send() method
        :param data: url and private mode 
        :return: VOID
        """
        target_hosts = data['url']
        target_url = data['is_private_mode']
        if "http://" not in target_hosts:
            target_hosts = "http://" + target_hosts
        if target_url == 1:
            target_hosts = target_hosts + "?private=true"
            request = "GET /%s HTTP/1.1\r\nHost: 127.0.0.1:17865\r\n\n" % target_hosts
            # print("in request_to_proxy:"+request)
            self._send(request)
        else:
            target_hosts = target_hosts + "?private=false"
            request = "GET /%s HTTP/1.1\r\nHost: 127.0.0.1:17865\r\n\n" % target_hosts
            self._send(request)

    def response_from_proxy(self):
        """
        the response from the proxy after putting the _recieve method to listen.
        handle the response, and then render HTML in browser. 
        This method must be called from web_proxy_server.py which is the home page of the app
        :return: the response from the proxy server
        """
        self.client_socket.listen(5)
        while True:
            raw_data = self._receive()
            raw_data.find('/')
            return "This is response proxy"

    def run(self, data):
        self.init_socket(data)
