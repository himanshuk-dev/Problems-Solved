#100:50,200: 25,75,300,10: 350, 15
# empty? yes
# single element? yes
# initialize result
# initialize current_queue, next_node
# insert root node in current_queue
# if there is elemnt in current_queue:
    # dequeue its data and store it in result
    #  if children on left, push to next queue
    #  if children on right, push to next queue
# if current queue is empty, increate level number and swap the two queues
# 
# 
#


from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def level_order_traversal(root):
    result = ''
    if not root:
        result = "None"
        return result
    else:
        current_queue = deque()
        dummy_node = TreeNode(0)
        
        current_queue.append(root)
        current_queue.append(dummy_node)
        
        while current_queue:
            temp = current_queue.popleft()
            result += str(temp.data)
            
            if temp.left:
                current_queue.append(temp.left)
            if temp.right:
                current_queue.append(temp.right)
            
            if current_queue[0] == dummy_node:
                current_queue.popleft()
                
                if current_queue:
                    result += ' : '
                    current_queue.append(dummy_node)
            else:
                result += ', '
                
        return result
            
            