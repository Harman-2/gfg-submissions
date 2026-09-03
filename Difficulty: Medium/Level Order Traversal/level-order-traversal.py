''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def levelOrder(self, root):
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            res.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
        