class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                x_1, y_1, r_1 = bombs[i]
                x_2, y_2, r_2 = bombs[j]
                dist = abs((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
                if dist <= r_1 ** 2:
                    graph[i].append(j)
                if dist <= r_2 ** 2:
                    graph[j].append(i)
                    
        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            
            out = 1
            for next_i in graph[i]:
                out += dfs(next_i, visited)
            
            return out
        
        max_count = 0
        for i in range(n):
            max_count = max(max_count, dfs(i, set()))
        return max_count

