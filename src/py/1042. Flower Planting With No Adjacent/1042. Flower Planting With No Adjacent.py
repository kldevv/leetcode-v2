class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # greedy
        
        graph = [set() for _ in range(n+1)]
        for u, v in paths:
            graph[u].add(v)
            graph[v].add(u)
            
        results = [0] * (n + 1)
        
        all_plants = {1, 2, 3, 4}
        for node in range(n+1):
            # randomly choose one plant that is not planted by the adjacent gardens
            results[node] = (all_plants - {results[neigh] for neigh in graph[node]}).pop()
        
        return results[1:]

