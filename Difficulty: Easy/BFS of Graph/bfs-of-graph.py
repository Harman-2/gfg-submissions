from collections import deque

class Solution:
    def bfs(self, adj):
       V = len(adj)
       visited = [False] * V
       res = []
       queue = deque()
       
       queue.append(0)
       visited[0] = True 
       
       while queue:
           node = queue.popleft()
           res.append(node)
           
           for neighbor in adj[node]:
              if not visited[neighbor]:
                 visited[neighbor]= True 
                 queue.append(neighbor)
       return res
       
       
        