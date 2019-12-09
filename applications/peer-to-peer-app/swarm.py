# -*- coding: utf-8 -*-
""" The tracker
This file has the class swarm that represents a swarm
where peers can share a resource.
"""


class Swarm(object):

    def __init__(self, resource_id):
        """
        Class constructor
        """
        self.peers = []  # the peers connected to this swarm
        self.resource_id = resource_id

    def add_peer(self, peer):
        """
        TODO: implement this method
        :param peer: add the peer object
        :return: VOID
        """
        self.peers.append(peer)
        return 0

    def delete_peer(self, peer):
        """
         TODO: implement this method
        :param peer_id: the client id of the peer
        :return: VOID
        """
        self.peers.remove(peer)
        return 0

    def peers(self):
        """
        TODO: implement this method
        :return: the list of peers connected to the swarm
        """
        peer_list = self.peers
        return peer_list

    def resource_id(self):
        """
        TODO: implement this method
        :return: the file id of the file that is being
                 shared by this swarm
        """
        file_id = self.resource_id()
        return file_id
