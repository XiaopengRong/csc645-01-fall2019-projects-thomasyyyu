import socketimport picklefrom time import time, ctimeimport threadingfrom tcpclienthandler import TCPClientHandler# TCPClientHandlerclass Client(object):    def __init__(self):        self.date = None        self.host = None        self.port = None        self.client_id = None        self.client_name = None        self.client_socket = None        self.client_msg = None    def connectToServer(self, host, port, client_name):        self.host = host        self.port = port        self.client_name = client_name        try:            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            self.client_socket.connect((self.host, self.port))            client_id = self.recieveDataFromServer()            self.client_id = int(client_id)            print("Connected to server with ip adress: " + self.host + " and port: " + str(self.port))            print("Client id assigned by server is: " + str(self.client_id))            self.sendDataToServer(self.client_name)            return True        except socket.error as msg:            print("Caught exception socket.error " + str(msg))            self.client_socket.close()            return False    def sendDataToServer(self, data):        data = pickle.dumps(data)        self.client_socket.send(data)    def recieveDataFromServer(self):        raw_data = self.client_socket.recv(4906)        data = pickle.loads(raw_data)        return data    def run(self):        host = str(input("Enter the server ip address: "))        port = int(input("Enter the server port: "))        clientName = str(input("Enter the clientName: "))        self.connectToServer(host, port, clientName)        while True:            tcpClientHandler = TCPClientHandler(client)            tcpClientHandler.printMenu()            option = int(input("Please select an option: "))            if option == 1:                tcpClientHandler.getUserListFromServer(self.client_socket)            if option == 2:                tcpClientHandler.sendmessagetouser(self.client_socket)            if option == 3:                tcpClientHandler.getmessagefromserver(self.client_socket)            if option == 4:                tcpClientHandler.createnewchannel()            if option == 5:                tcpClientHandler.p2pconnect()            if option == 6:                tcpClientHandler.disconnectserver()# run the client when the file is executedclient = Client()client.run()