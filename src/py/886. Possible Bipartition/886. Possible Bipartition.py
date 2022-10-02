class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        colors = [0] * n
        
        def dfs(i, to_color):
            colors[i] = to_color
            for next_i in graph[i]:
                if colors[next_i] == to_color:
                    return False
                if colors[next_i] == 0 and not dfs(next_i, -to_color):
                    return False
            return True
        
        for i in range(n):
            if colors[i] == 0 and not dfs(i, 1):
                    return False
        return True

