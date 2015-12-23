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
        print

    def delete_key(self, val):
        temp = self.head
        if temp.data == val:
            self.head = temp.next
            return 
        while temp.next and temp.next.data != val:
            temp = temp.next
        temp.next = temp.next.next

    def delete_on_position(self, pos):
        temp = self.head
        if not pos:
            self.head = temp.next
            return
        pos -= 1
        while pos and temp:
            pos -= 1
            temp = temp.next
        if not temp.next:
            print "Nothing to delete"
            return
        temp.next = temp.next.next

def main():
    #create link list and node
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    #now combine nodes
    llist.head.next = second
    second.next = third
    third.next = fourth
    llist.printList()

    #delete key
    #llist.delete_key(4)
    llist.delete_on_position(4)
    #print list
    llist.printList()

if __name__ == '__main__':
    main()

