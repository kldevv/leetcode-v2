class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * n * 2
        
    def update(self, i, value):
        i += self.n 
        
        self.data[i] = value
        while i >= 1:
            self.data[i >> 1] = max(self.data[i], self.data[i^1])
            i >>= 1
        
    def query(self, start, end):
        start += self.n
        end += self.n
        out = 0
        
        while start < end:
            if start & 1:
                out = max(out, self.data[start])
                start += 1
            if end & 1:
                end -= 1
                out = max(out, self.data[end])
            start >>= 1
            end >>= 1
        
        return out

            
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        sgt = SegmentTree(max(nums) + 1)
        out = 0
        
        for num in nums:
            cur_len = sgt.query(max(0, num-k), num) + 1
            out = max(out, cur_len)
            sgt.update(num, cur_len)
        
        
        return out
            