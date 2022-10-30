class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        max_num = max(arr)
        min_num = min(arr)
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for i in range(min_num, max_num + 1):
            while i in freq and freq[i]:
                freq[i] -= 1
                if i >= 0 and freq.get(i*2, 0):
                    freq[i*2] -= 1
                elif i < 0 and freq.get(i/2, 0):
                    freq[i/2] -= 1
                else:
                    return False
        return True