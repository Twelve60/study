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
    
    def print_list(self):
        entries = []
        current_node = self.head

        while current_node.next != None:
            entries.append(current_node.data)
            current_node = current_node.next

        entries.append(current_node.data)

        return " -> ".join(entries)

    def length_iterative(self):
        count = 0
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            count += 1

        return count + 1
    
    def length_recursive(self, node):
        if not node:
            return
        else:
            return 1 + self.length_recursive(node.next)
    
    def get_count(self):
        return self.length_recursive(self.head)            


ll = LinkedList('a')
ll.append('b')
ll.append('c')
ll.append('d')

print ll.print_list()
print ll.length_iterative()
print ll.get_count()
