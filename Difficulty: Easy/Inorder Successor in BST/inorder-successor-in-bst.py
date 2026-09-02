'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrderSuccessor(self, root, k):
        res = None
        curr = root
        while curr:
            if k.data < curr.data:
                res = curr
                curr = curr.left
            else:
                curr = curr.right
        return res.data if res else -1
       