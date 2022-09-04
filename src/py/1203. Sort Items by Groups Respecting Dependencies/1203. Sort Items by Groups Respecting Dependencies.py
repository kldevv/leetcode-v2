class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:        
        # reassign group number to -1
        for i, group_num in enumerate(group):
            if group_num == -1:
                group[i] = m
                m += 1
        
        # items level
        items_graph = [[] for _ in range(n)]
        items_in_degree = [0] * n
        
        # group level
        group_graph = [set() for _ in range(m)]
        group_in_degree = [0] * m
        
        # build graph and degree
        for u, vs in enumerate(beforeItems):
            u_group = group[u]
            for v in vs:
                v_group = group[v]
                
                # connect item level
                items_in_degree[u] += 1
                items_graph[v].append(u)
                
                # connect groups level
                if v_group != u_group and u_group not in group_graph[v_group]:
                    group_in_degree[u_group] += 1
                    group_graph[v_group].add(u_group)
        
        
        def top_sorted(in_degrees, graph):
            result = []
            q = [node for node, degree in enumerate(in_degrees) if degree == 0]
            
            for node in q:
                result.append(node)
                for neigh in graph[node]:
                    in_degrees[neigh] -= 1
                    if in_degrees[neigh] == 0:
                        q.append(neigh)
            
            return result
        
        # sort
        groups_order = top_sorted(group_in_degree, group_graph)
        items_order = top_sorted(items_in_degree, items_graph)
        
        # group ordered items by group
        items_in_groups_order = [[] for _ in range(m)]
        for item in items_order:
            items_in_groups_order[group[item]].append(item)
        
        # concate ordered items by group ordering by ordered group
        result = []
        for group_num in groups_order:
            result += items_in_groups_order[group_num]
            
        return result if len(result) == n else []

