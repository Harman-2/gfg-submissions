""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        i = head # main pointer 
        j = head # reference pointer 
        
        for count in range(k):
            if j is None:
                return -1
            j = j.next
        
        while j:
            i = i.next 
            j = j.next 
        return i.data
        