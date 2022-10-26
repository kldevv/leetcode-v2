class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(target)
        cnt = Counter(nums)
        out = 0
        for num in cnt.keys():
            if target[:len(num)] == num:
                suffix = target[len(num):]
                if suffix == num:
                    out += cnt[num] * (cnt[num]-1)
                elif suffix in cnt:
                    out += cnt[num] * cnt[suffix]
        return out