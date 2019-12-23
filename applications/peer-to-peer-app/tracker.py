# -*- coding: utf-8 -*-
""" The tracker
This file implements the Tracker class. The tracker has two main functionalities
 (1) A client connects to a tracker, and a tracker sends
all the peers ip addresses and ports connected to the swarm that are sharing
the same resource. Since a tracker can handle more than one swarm, then the
swarm needs to be identified with a id (i.e the file id that is being shared
in the swarm)
 (2) When a peers change status (become leechers or seeders) they must inform
 the tracker, so the tracker can update that info in the swarm where they are
 sharing the resource

"""

from _thread import *
from server import Server


class Tracker(Server):
    PORT = 12000
    IP_ADDRESS = "127.0.0.1"

    def __init__(self, ip_address=None, port=0):
        """
        TODO: finish constructor implementation (if needed)
        If parameters ip_address and port are not set at the object creation time,
        you need to use the default IP address and the default port set in the class constants.
        :param ip_address:
        :param port:
        """
        Server.__init__(self)
        self.port = port
        self.ip = ip_address
        # the list of swarms that this tracker keeps
        self.swarms = []

    def add_swarm(self, swarm):
        """
        Already implemented
        Add a Swarm object to the swarms list of the tracker
        :param swarm:
        :return:
        """
        self.swarms.append(swarm)

    def remove_swarm(self, peer):
        """
        TODO: implement this method
        Given a resource id, remove the swarm from the tracker
        that is sharing this resource id.
        This happens normally when there is no seeder sharing
        this resource.
        :param resource_id:
        :return: VOID
        """
        self.swarms.remove(peer)
        return 0

    def add_peer_to_swarm(self, peer):
        """
        TODO: implement this method
        Based on the resource_id provided, iterate over the
        swarms list, and when resource_id matchs, add the
        new peer to the swarm.
        :param peer:
        :param resource_id:
        :return: VOID
        """
        if peer not in self.swarms:
            self.add_swarm(peer)
        else:
            print("resource_id did not match swarms list.")
        return 0

    def change_peer_status(self):
        """
        TODO: implement this method
        When a peers in a swarm report a change of status
        (leecher or seeder) then, get the swarm object from
        the swarm list, and update the status in the swarm of
        such peer.
        :return: VOID
        """

        return 0

    def send_peers(self, peer_socket):
        """
        TODO: implement this method
        Iterate the swarms list, and find the one which match with
        the resource id provided as a parameter. Then, serialize the
        swarm and send the swarm object to the peer requesting it.
        :param peer_socket: the peer socket that is requesting the info
        :param resource_id: the resource id to identify the swarm
               sharing this resource
        :return: VOID
        """
        return 0

    def run(self):
        print("Server Info")
        if self.ip is None:
            self.ip = self.IP_ADDRESS
        if self.port == 0:
            self.port = self.PORT
        print("IP Address: " + self.ip)
        print("port listening: " + str(self.port))
        print("waiting for connections...")
        self.server_socket.bind((self.ip, self.port))
        self.listen()
        while True:
            try:
                self.accept()
                self.sendData(self.client_id)
                deserialized_data = self.recieve(self.MAX_ALLOCATE_SIZE)
                if self.client_id not in self.global_dic:
                    self.global_dic[self.client_id] = deserialized_data
                start_new_thread(self.threaded_client, (self.client_sock, self.client_id))
                print("Client: " + str(deserialized_data)+" with client ID: " + str(self.client_id) + " has connected to this server")
            except:
                print("Reach the maximum number of 5 people")
                break


server = Tracker()
server.run()
