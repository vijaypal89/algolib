#!/usr/bin/python

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next

def main():
    #create link list and node
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    #now combine nodes
    llist.head.next = second
    second.next = third
    llist.printList()

if __name__ == '__main__':
    main()

