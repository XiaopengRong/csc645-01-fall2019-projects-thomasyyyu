import socket
import pickle
from _thread import *
import threading
lock = threading.Lock()


HOST = '127.0.0.1'
PORT = 17865
MAX_NUM_CONNECTIONS = 5

print("Server Info")
print("IP Address: " + HOST)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((HOST, PORT))
except socket.error as e:
    print((str(e)))
server.listen(MAX_NUM_CONNECTIONS)
print("port listening: " + str(PORT))
print("waiting for connections...")

while True:
    try:
        client_sock, addr = server.accept()
        client_id = addr[1]
        #print("Client " + str(client_id)+" has connected")
        cid = pickle.dumps(client_id)
        client_sock.sendall(cid)
        while True:
            try:
                data_from_client = client_sock.recv(4096)
                data = pickle.loads(data_from_client)
                print("Client " + data + " with clientid: " + str(client_id) + " has connected to this server")
            except:
                client_sock.close()
    except:
        server.close()

            #request_from_client = client_sock.recv(4096)
            #data = pickle.loads(request_from_client)
            #client_msg = data['msg_from_client']
            #ID = data['Id_from_client']
            #print("Client says: "+client_msg)
            #server_msg = "Hello from server!"
            #server_response = {"client_id": client_id, "msg_from_server": server_msg}
            #server_serialized = pickle.dumps(server_response)
            #client_sock.send(server_serialized)
            #client_sock.close()



