class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # nlogm, m = max(nums)
        def gcd(a, b):
            if b == 0:
                return abs(a)
            return gcd(b, a % b)
            
        last_gcd_cnt = defaultdict(int)
        out = 0
        for num in nums:
            cur_gcd_cnt = defaultdict(int)
            if num % k == 0:
                cur_gcd_cnt[num] = 1
                # bound by log(max(max))
                for last_gcd, cnt in last_gcd_cnt.items():
                    cur_gcd_cnt[gcd(num, last_gcd)] += cnt
            out += cur_gcd_cnt[k]
            last_gcd_cnt = cur_gcd_cnt
        return out

