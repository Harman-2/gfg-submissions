'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def isHeap(self, root):
        if not root:
            return True
            
        res = []
        queue = deque([root])
        null_seen = False
        
        while queue:
            node = queue.popleft()
            
            if node is None:
              null_seen = True
              continue
        
            if null_seen:
              return False
        
            if node.left:
              if node.left.data>node.data:
                  return False
              queue.append(node.left)
            else:
              queue.append(None)
        
            if node.right:
               if node.right.data>node.data:
                return False
               queue.append(node.right)
            else:
               queue.append(None)
        return True 
    
            
        