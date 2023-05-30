#!/usr/bin/python3

"""Define class node for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node with constructor.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList with constructor."""
        self.__head = None

    def sorted_insert(self, value):
        """ insert node in the correct sorted position """
        newnode = Node(value)
        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = newnode
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            newnode.next_node = temp.next_node
            temp.next_node = newnode

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        val = []
        temp = self.__head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(val))
