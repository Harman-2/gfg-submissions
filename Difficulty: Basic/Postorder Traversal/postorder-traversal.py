''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        res = []
        
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            traverse(root.right)
            res.append(root.data)
        traverse(root)
        return res
        
        
        