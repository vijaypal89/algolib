#!/usr/bin/python

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def main():
    #create link list and node
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    #now combine nodes
    llist.head.next = second
    second.next = third


if __name__ == '__main__':
    main()

