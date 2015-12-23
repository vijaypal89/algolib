#!/usr/bin/python

import sys

class Node:
    def __init__(self, data=None):
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

def reverse(current):
    s = LinkedList()
    prev = s.head
    next = Node()
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
        s.head = prev
    return s

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
    ll = reverse(ll.head)
    ll.printList()

if __name__ == '__main__':
    main()

