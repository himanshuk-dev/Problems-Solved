class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('node doesnt exist')
            return
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_node(self, key):
        curr_node = self.head
        
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None
        if curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
            
        if curr_node is None:
            return
        
        prev.next = curr_node.next
        curr_node = None