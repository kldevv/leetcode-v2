class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        p = list(range(256))
        rank = [0] * 256
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if rank[y] > rank[x]:
                p[x] = y
            else:
                p[y] = x
                rank[x] += int(rank[x] == rank[y])
        
        for e in equations:
            if e[1] == "=":
                union(ord(e[0]), ord(e[-1]))
        
        for e in equations:
            if e[1] == "!" and find(ord(e[0])) == find(ord(e[-1])):
                return False
        
        return True

