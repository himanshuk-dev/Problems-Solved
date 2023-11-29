# recursively calculate sum
# sum store
# function call
# if there is no node, return empty
# if node has no left and right node, store running sum to sum
# recursively call the finction on left node
# recursively call the finction on right node



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return
    
    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:  # If it's a leaf node
        sums.append(new_running_sum)
        return
    
    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.right, new_running_sum, sums)

def branchSums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums
