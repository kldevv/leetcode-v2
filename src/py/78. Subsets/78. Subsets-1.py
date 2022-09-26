class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            new_out = []
            for prev_set in out:
                new_out.append(prev_set + [num])
            out += new_out
        return out

