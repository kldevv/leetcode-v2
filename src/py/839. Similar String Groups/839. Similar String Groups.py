class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            if rank[x] > rank[y]:
                p[y] = x
            else:
                p[x] = y
                rank[y] += int(rank[x] == rank[y])
        
        n = len(strs)
        p = list(range(n))
        rank = [0] * n
        
        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]):
                    i_p = find(i)
                    j_p = find(j)
                    if i_p != j_p:
                        union(i_p, j_p)
                        
        for i in range(n):
            find(i)
        return len(set(p))
                