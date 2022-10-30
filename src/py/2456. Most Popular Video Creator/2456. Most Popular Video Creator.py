class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        view_sum = defaultdict(int)
        max_view_sum = 0
        for c, v in zip(creators, views):
            view_sum[c] += v
            max_view_sum = max(max_view_sum, view_sum[c])
        
        max_view_creators = set(c for c in creators if view_sum[c] == max_view_sum)
        
        out = {}
        for i in range(len(creators)):
            creator = creators[i]
            if creator in max_view_creators:
                if creator not in out \
                    or out[creator][1] < views[i] \
                        or out[creator][1] == views[i] and ids[i] < out[creator][0]:
                    out[creator] = [ids[i], views[i]]
        
        return [(k, v[0]) for k, v in out.items()]

