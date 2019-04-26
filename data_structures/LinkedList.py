#!/usr/bin/env python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data, head=None):
        self.node = Node(data)
        self.head = head

        if not self.head:
            self.head = self.node
        
    def append(self, data):
        node = Node(data)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node

        return

ll = LinkedList('a')
ll.append('b')
ll.append('c')
ll.append('d')

print "{} -> {} -> {} -> {}".format( ll.head.data,
                                     ll.head.next.data,
                                     ll.head.next.next.data,
                                     ll.head.next.next.next.data )