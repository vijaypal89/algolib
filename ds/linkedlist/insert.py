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

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            print "prev_node is not defined"

    def insert_end(self, data):
        new_node = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def main():
    #create link list and node
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    #now combine nodes
    llist.head.next = second
    second.next = third

    #insert to list
    llist.insert_end(50)
    llist.insert_front(-40)
    llist.insert_after(llist.head, 110)

    #print list
    llist.printList()

if __name__ == '__main__':
    main()

