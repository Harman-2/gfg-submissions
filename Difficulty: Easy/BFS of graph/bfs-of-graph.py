from collections import deque

class Solution:
    def bfs(self, adj):
        V = len(adj)
        visited = [False] * V
        res = []

        
        q = deque([0])
        visited[0] = True

        while q:
            curr = q.popleft()
            res.append(curr)

            
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        return res