class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        # path compression
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        # x -> y
        x_p = self.find(x)
        y_p = self.find(y)

        # already in the set (cycle)
        if x_p == y_p:
            return False

        self.parents[y_p] = x_p
        
        return True
    

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        
        in_edge = dict()
        
        dup_edges = None
        for edge in edges:
            par, chi = edge
            if chi in in_edge:
                dup_edges = (in_edge[chi], edge)
            in_edge[chi] = edge
        
        ds = DisjointSet(n)
        for edge in edges:
            if dup_edges and edge == dup_edges[1]:
                continue
                
            par, chi = edge
            
            if not ds.union(par, chi):
                return dup_edges[0] if dup_edges else edge
            
        return dup_edges[1]
            