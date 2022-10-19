class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        p = list(range(n))
        rank = [0] * n
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            x_p = find(x)
            y_p = find(y)
            if rank[x_p] < rank[y_p]:
                p[x_p] = y_p
            else:
                p[y_p] = x_p
                rank[x_p] += int(rank[x_p] == rank[y_p])
        
        
        for u, v in pairs:
            union(u, v)
        
        sets = defaultdict(list)
        for i, c in enumerate(s):
            i_p = find(i)
            sets[i_p].append(c)
        
        sets = {k: [sorted(v), 0] for k, v in sets.items()}
        
        out = [None] * n
        
        for i in range(n):
            group = sets[find(i)]
            out[i] = group[0][group[1]]
            group[1] += 1
        return "".join(out)
