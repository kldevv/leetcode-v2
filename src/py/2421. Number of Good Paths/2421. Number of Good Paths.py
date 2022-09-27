class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        for u, v in edges:  
            # we'll construct graph with only good path
            if vals[u] >= vals[v]:
                graph[u].append(v)
            if vals[v] >= vals[u]:
                graph[v].append(u)
        
        same_val = collections.defaultdict(list)
        for i, val in enumerate(vals):
            same_val[val].append(i)

        f = list(range(n))
        rank = [0] * n
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        
        out = n
        # start from the samllest value to construct the graph
        # so if all the nodes in the same group have a good path to another
        for val in sorted(list(same_val.keys())):
            for node in same_val[val]:
                for next_node in graph[node]:
                    nnf = find(next_node)
                    nf = find(node)
                    # union by rank
                    if rank[nf] < rank[nnf]:
                        f[nf] = nnf
                    elif rank[nf] > rank[nnf]:
                        f[nnf] = nf
                    else:
                        f[nnf] = nf
                        rank[nf] += 1
            
            # examine the distribution of the same val nodes
            # because the properties of the tree, there is only one path from node a to b
            f_val_count = collections.defaultdict(int)
            for node in same_val[val]:
                f_val_count[find(node)] += 1
            
            out += sum(count*(count-1)//2 for count in f_val_count.values())
        
        return out