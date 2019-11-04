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

    # def init_socket(self, data):

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

    def request_to_proxy(self, data):
        """
        Create the request from data 
        request must have headers and can be GET or POST. depending on the option
        then send all the data with _send() method
        :param data: url and private mode 
        :return: VOID
        """
        target_url = data['url']
        target_mode = data['is_private_mode']
        if "http://" not in target_url:
            target_url = "http://" + target_url
        if target_mode == 1:
            target_url = target_url + "?priavte=true"
            request = "GET /%s HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: " \
                      "Firefox/3.6.10\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-us," \
                      "en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7\r\n" \
                      "Keep-Alive: 115\r\nConnection: keep-alive\r\n\r\n" % target_url
            data = pickle.dumps(request)
            self.client_socket.sendall(data)
            return 0
        else:
            target_url = target_url + "?private=false"
            request = "GET /%s HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: " \
                      "Firefox/3.6.10\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-us," \
                      "en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7\r\n" \
                      "Keep-Alive: 115\r\nConnection: keep-alive\r\n\r\n" % target_url
            data = pickle.dumps(request)
            self.client_socket.sendall(data)
            return 0

    def response_from_proxy(self):
        """
        the response from the proxy after putting the _recieve method to listen.
        handle the response, and then render HTML in browser. 
        This method must be called from web_proxy_server.py which is the home page of the app
        :return: the response from the proxy server
        """
        data = self.client_socket.recv(1000000000)
        de_data = pickle.loads(data)
        return de_data

    def run(self, data):
        host = '127.0.0.1'
        port = 13000
        self._connect_to_server(host, port, data)
