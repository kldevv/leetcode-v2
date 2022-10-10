class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        f = list(range(26))
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        
        def union(x, y):
            fx = find(x)
            fy = find(y)
            if fx < fy:
                f[fy] = fx
            else:
                f[fx] = fy
        
        for c1, c2 in zip(s1, s2):
            c1_i = ord(c1) - ord('a')
            c2_i = ord(c2) - ord('a')
            union(c1_i, c2_i)
        
        out = []
        for c in baseStr:
            fc = find(ord(c) - ord('a'))
            out.append(chr(fc + ord('a')))
        return "".join(out)
                    