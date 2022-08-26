class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        
        for u, v in richer:
            graph[v].append(u)
        
        results = [None] * n
        
        def dfs(p):
            if results[p] is None:
                results[p] = p
                for poorer in graph[p]:
                    cand = dfs(poorer)
                    if  quiet[cand] < quiet[results[p]]:
                        results[p] = cand
                        
            return results[p]
        
        return map(dfs, range(n))