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
    
    def length_recursive(self, node, count):
        if not count:
            count = 0
        
        if not node:
            return
        
        elif node.next is None:
            count += 1
            return count
    
        count += 1
        return self.length_recursive(node.next, count)
    
    def get_count(self):
        return self.length_recursive(self.head, count=None)            


ll = LinkedList('a')
ll.append('b')
ll.append('c')
ll.append('d')

print "list = {}".format(ll.print_list())
print "Length via iteration = {}".format(ll.length_iterative())
print "Length via recursion = {}".format(ll.get_count())
