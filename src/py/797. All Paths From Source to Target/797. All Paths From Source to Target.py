class Solution:
    def __init__(self):
        self.paths = []
        self.graph = []
        self.n = 0
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.n = len(graph) - 1
        
        self.dfs(0, [0])
        
        return self.paths
    
    def dfs(self, node, path):
        if node == self.n:
            self.paths.append(path)
            return
        
        for neig in self.graph[node]:
            self.dfs(neig, path+[neig])
    