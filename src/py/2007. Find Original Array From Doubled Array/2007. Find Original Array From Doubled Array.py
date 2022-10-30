class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        max_num = max(changed)
        freq = [0] * ((max_num * 2) + 1)
        for num in changed:
            freq[num] += 1
            
        out = []
        for i in range(max_num+1):
            while freq[i]:
                freq[i] -= 1
                if freq[i * 2]:
                    freq[i * 2] -= 1
                    out.append(i)
                else:
                    return []
        return out

