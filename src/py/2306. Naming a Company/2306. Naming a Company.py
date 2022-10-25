class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)
        for idea in ideas:
            groups[idea[0]].add(idea[1:])
        
        out = 0
        for i in range(26):
            for j in range(i+1, 26):
                i_c = chr(i+ord('a'))
                j_c = chr(j+ord('a'))
                if i_c not in groups or j_c not in groups:
                    continue
                same_suffix = len(groups[i_c] & groups[j_c])
                out += (len(groups[i_c])-same_suffix) * (len(groups[j_c])-same_suffix)
        return out * 2

