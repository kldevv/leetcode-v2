class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # dfs
        
        # fisrt use dfs to find the maximum distance to each node
        def dfs(node, dist):
            n = 0
            while node != -1 and node not in dist:
                dist[node] = n
                node = edges[node]
                n += 1
        
        max_dist_node1 = {}
        dfs(node1, max_dist_node1)
        max_dist_node2 = {}
        dfs(node2, max_dist_node2)
        
        n = len(edges)
        
        # compare and find the minimum distance node to both node1 and node2
        min_dist = n
        min_dist_idx = -1
        for i in range(n):
            if i in max_dist_node1 and i in max_dist_node2:
                cand_min_dist = max(max_dist_node1[i], max_dist_node2[i])
                if cand_min_dist < min_dist:
                    min_dist = cand_min_dist
                    min_dist_idx = i
        return min_dist_idx
            
            
        