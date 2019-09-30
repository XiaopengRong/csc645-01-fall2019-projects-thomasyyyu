import socket
import pickle
from _thread import *
import threading
from time import time, ctime

lock = threading.Lock()

global_array = {}
sort_data = {" ": [" "]}


def thread(client_sock, client_id_fm):
    while True:
        data_from_client_string = client_sock.recv(4096)
        data_from_client = pickle.loads(data_from_client_string)
        if not data_from_client:
            print("Disconnect from server")
            break
        if data_from_client['option'] == "1":
            userList = ""
            for user_keys, user_value in global_array.items():
                userList = userList + str(user_keys) + ": " + user_value + "\n"
            client_sock.send(pickle.dumps(userList))
        elif data_from_client['option'] == "2":
            client_id = data_from_client['userId']
            msg = data_from_client['msgs']
            if client_id in sort_data:
                sort_data[client_id].append(msg)
            else:
                sort_data[client_id] = [msg]
        elif data_from_client['option'] == "3":
            if str(client_id_fm) in sort_data:
                msgL = sort_data[str(client_id_fm)]
                client_sock.send(pickle.dumps(msgL))
            else:
                msgsL = ["not_found_message_in_sort_data"]
                client_sock.send(pickle.dumps(msgsL))

        elif data_from_client['option'] == "4":
            print("in 4")
    client_sock.close()


def Main():
    HOST = '127.0.0.1'
    PORT = 17865
    print("Server Info")
    print("IP Address: " + HOST)
    print("port listening: " + str(PORT))
    print("waiting for connections...")
    MAX_NUM_CONNECTIONS = 5
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(MAX_NUM_CONNECTIONS)
    while True:
        try:
            client_sock, addr = server.accept()
            client_id = addr[1]
            cid = pickle.dumps(client_id)
            client_sock.sendall(cid)
            data_from_client = client_sock.recv(4096)
            serialized_data = pickle.loads(data_from_client)
            if client_id not in global_array:
                global_array[client_id] = serialized_data
            start_new_thread(thread, (client_sock, client_id))
            print("Client " + serialized_data + " with clientid: " + str(client_id) + " has connected to this server")
        except:
            print("Reach the maximum number of 5 people")
            break


if __name__ == '__main__':
    Main()
