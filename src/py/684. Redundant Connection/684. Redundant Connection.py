class DisjointSet:
    def __init__(self, n):
        self.ranks = [0] * n
        self.parents = list(range(n))

    def find(self, x):
        # path compression
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        # union by ranks
        x_p = self.find(x)
        y_p = self.find(y)

        # already in the set (cycle)
        if x_p == y_p:
            return False

        x_p_rank = self.ranks[x_p]
        y_p_rank = self.ranks[y_p]

        if x_p_rank < y_p_rank:
            return self.union(y, x)

        if x_p_rank == y_p_rank:
            self.ranks[x_p] += 1

        self.parents[y_p] = x_p
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        ds = DisjointSet(n)
        for edge in edges:
            if not ds.union(*edge):
                return edge

        return []








