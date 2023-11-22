class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def depthFirstSearch(self, array):
        # Append the current node's name to the array
        array.append(self.name)
        
        # Recursively call depthFirstSearch on each child node
        for child in self.children:
            child.depthFirstSearch(array)
        
        return array
