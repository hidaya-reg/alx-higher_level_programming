#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """class Node that defines node of a singly linked list """

    def __init__(self, data, next_node=None):
        """"Instantiation with data and next node"""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node

    @property
    def data(self):
        """Property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, data):
        """Property to set data"""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        """property to retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Property setter to set next node"""
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """a class that defines a singly linked list"""

    def __init__(self):
        """Simple instantiation of singly linked list"""
        self.__head = None

    def __str__(self):
        """printable singly linked list"""
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """insert a new Node into the correct sorted position"""

        new = Node(value)
        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new.next_node = current.next_node
        current.next_node = new
