class Solution:
    def dfs(self, graph, node, visited):
        visited[node] = True
        for i in graph[node]:
            if visited[i] == False:
                self.dfs(graph, i, visited)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])
        graph = {i:[] for i in range(m)}
        
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        visited = [False for _ in range(m)]
        ans = 0
        for i in range(m):
            if visited[i] == False:
                ans += 1
                self.dfs(graph, i, visited)
        
        return ans
