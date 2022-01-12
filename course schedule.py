class Solution:
    def dfs(self, graph, visit, i):
        if i in visit:
            return False
        if graph[i] == []:
            return True
        visit.add(i)
        for val in graph[i]:
            if not self.dfs(graph, visit, val):
                return False
        visit.remove(i)
        graph[i] = []
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for i, val in prerequisites:
            graph[i].append(val)
        visit = set()
        
        for i in range(numCourses):
            if not self.dfs(graph, visit, i):
                return False
        return True
