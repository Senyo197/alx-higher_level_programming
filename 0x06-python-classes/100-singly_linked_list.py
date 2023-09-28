#!/usr/bin/python3
"""Define node classes"""


class Node:
    """Represents a Node Class for singly linked node"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data to be added.
            next_node (Node): The next node in the data.
        """
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """Retrieve the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the node.
        Arg:
            value (int): Value of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the data of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the node.
        Arg:
            value (int): Value of the node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a SinglyLinkedList"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Set the value of the node.
        Arg:
            value (int): Value of the node.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while (curr.next_node is not None and curr.next_node.data < value):
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = []
        curr = self.__head
        while curr:
            result.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(result)
