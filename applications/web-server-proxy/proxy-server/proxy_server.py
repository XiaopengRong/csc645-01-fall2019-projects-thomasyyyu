import os, sys, _thread, socket
from proxy_thread import ProxyThread


class ProxyServer(object):

    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 17865
        self.BACKLOG = 50
        self.MAX_DATA_RECV = 4096

    def run(self):
        try:
            my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_sock.bind((self.HOST, self.PORT))
            my_sock.listen(self.BACKLOG)
            print("Socket listening...")
            while True:
                self.accept_clients(my_sock)
        except socket.error as message:
            print(message)

    def accept_clients(self, sock):
        """
        Accept clients that try to connect. 
       :return: 
        """
        client_sock, addr = sock.accept()
        client_id = addr[1]
        print("Client_id is :" + str(client_id))
        self.proxy_thread(client_sock, str(client_id))

    def proxy_thread(self, conn, client_addr):
        """
        I made this method for you. It is already completed and no need to modify it. 
        This already creates the threads for the proxy is up to you to find out where to put it.
        Hint: since we are using only  non-persistent connections. Then, when a clients connects, 
        it also means that it already has a request to be made. Think about the difference 
        between this and assign#1 when you created a new thread. 
        :param conn: 
        :param client_addr: 
        :return: 
        """
        proxy_thread = ProxyThread(conn, client_addr)
        proxy_thread.init_thread()
        return 0


server = ProxyServer()
server.run()
