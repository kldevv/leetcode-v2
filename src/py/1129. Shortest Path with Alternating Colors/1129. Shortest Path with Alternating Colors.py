class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 0: red, 1: blue
        graph = [collections.defaultdict(set), collections.defaultdict(set)]
        
        for u, v in redEdges:
            graph[0][u].add(v)
        for u, v in blueEdges:
            graph[1][u].add(v)
        
        # 0: red, 1: blue
        results = [[-1, -1] for _ in range(n)]
        # node 0 to node 0 requires 0 path count
        results[0][0] = 0
        results[0][1] = 0
        
        # node, color
        q = [[0, 0], [0, 1]]
        
        for node, color in q:
            for neigh in graph[1-color][node]:
                if results[neigh][color] == -1:
                    results[neigh][color] = results[node][1-color] + 1
                    q.append([neigh, 1-color])
        
        return [min(result[0], result[1]) if result[0] != -1 and result[1] != -1 else max(result[0], result[1]) for result in results]
            
        
        
        
        