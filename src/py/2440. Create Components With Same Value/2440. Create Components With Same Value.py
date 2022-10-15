class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        
        if len(set(nums)) == 1:
            return n - 1
        
        total = sum(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            nonlocal cnt
            
            cur_sum = nums[node]
            for child in graph[node]:
                if child != parent:
                    cur_sum += dfs(child, node)
            
            if cur_sum == target:
                cnt -= 1
                return 0
            
            return cur_sum
        
        i = 2
        out = 0
        while i * i <= total:
            if total % i == 0:
                target = i
                cnt = total // i
                dfs(0, -1)
                if cnt == 0:
                    out = max(out, total // i - 1)
                
                target = total // i
                cnt = i
                dfs(0, -1)
                if cnt == 0:
                    out = max(out, i - 1)
            i += 1
        return out

