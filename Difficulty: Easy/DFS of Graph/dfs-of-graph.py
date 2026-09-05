class Solution:
    def dfs(self, adj):
       V = len(adj)
       visited = [False]*V 
       res = []
       stack = [0]
       
       while stack:
           curr = stack.pop()
           if not visited[curr]:
               visited [curr]=True
               res.append(curr)
               
           for neighbor in reversed(adj[curr]):
               if not visited[neighbor]:
                   stack.append(neighbor)
       return res
        