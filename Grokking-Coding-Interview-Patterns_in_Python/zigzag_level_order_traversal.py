#    [3, 5, null, -4, 7, 8, 9, 20] => [[3], [5], [-4, 7], [9, 8], [20]]
# binary tree? yes   
# empty? yes
# single? yes
# 
# add root of the tree to dq
# set flag 'reverse' to False
# result storage []
# level = 0
# iterate over dq till is not empty
# if level % 2 != 0:
    # reverse = True
# if reverse:
    # remove from right (.pop(-1))
    # store in result
# else:
    # remove from left (.leftpop())
    # store in result
# level += 1
#
# return result


from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigzag_level_order(root):
    if not root:
        return []

    results = []
    dq = deque([root])
    level = 0  # Keep track of current level

    while dq:
        level_length = len(dq)
        current_level = []

        for i in range(level_length):
            if level % 2 == 0:  # Even levels (from left to right)
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:  # Odd levels (from right to left)
                node = dq.pop()
                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left)

            current_level.append(node.data)

        results.append(current_level)
        level += 1

    return results
