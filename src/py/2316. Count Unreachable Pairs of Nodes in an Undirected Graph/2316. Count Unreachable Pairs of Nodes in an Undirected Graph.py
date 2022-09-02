class DisjointSet:
    def __init__(self, n):
        self.ranks = [0] * n
        self.counts = [1] * n
        self.pars = [i for i in range(n)]
        
    def _find(self, node):
        if self.pars[node] != node:
            self.pars[node] = self._find(self.pars[node])
        return self.pars[node]
        
    def union(self, A, B):
        parsA = self._find(A)
        parsB = self._find(B)
        
        if parsA == parsB:
            return
        
        if self.ranks[parsA] < self.ranks[parsB]:
            return self.union(B, A)
        
        if self.ranks[parsA] == self.ranks[parsB]:
            self.ranks[parsA] += 1
        
        self.pars[parsB] = self.pars[parsA]
        self.counts[parsA] += self.counts[parsB]
        self.counts[parsB] = 0

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # union find
        
        if len(edges) == 0:
            return n * (n-1) // 2
        
        ds = DisjointSet(n)
        
        for A, B in edges:
            ds.union(A, B)
            
        # pair-wise multiplication sum    
        # we even have a close form if the array is continously increasing, e.g. range(10)
        unreachable_pairs = 0
        pre_pair_accum = ds.counts[0]
        for i in range(1, n):
            unreachable_pairs += pre_pair_accum * ds.counts[i]
            pre_pair_accum += ds.counts[i]

        return unreachable_pairs
