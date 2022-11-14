class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        lcms = Counter()
        out = 0
        for num in nums:
            lcms[num] += 1
            tmp = Counter()
            for val, cnt in lcms.items():
                # val is all the possible subarray's lcm ends at i-1
                candidate = lcm(val, num)
                if candidate == k:
                    out += cnt
                if k % candidate == 0:
                    tmp[candidate] += cnt
            lcms = tmp
        return out