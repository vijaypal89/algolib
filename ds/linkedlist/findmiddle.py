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
    def printmiddle(self):
        f1 = self.head
        f2 = self.head
        while f2 and f2.next:
            f1 = f1.next
            f2 = f2.next
            if f2:
                f2 = f2.next
        print f1.data

def main():
    ll = LinkedList()
    first = Node("aa")
    ll.head = first
    second = Node("ab")
    third = Node("ac")
    fourth = Node("ad")
    five = Node("ae")
    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = five
    ll.printList()
    ll.printmiddle()

if __name__ == '__main__':
    main()

