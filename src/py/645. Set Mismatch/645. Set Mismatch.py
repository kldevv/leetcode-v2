class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor, xor1, xor0 = 0, 0, 0
        n = len(nums) + 1
        
        for num in nums:
            xor ^= num
        for i in range(1, n):
            xor ^= i
        least_significant_bit = xor & -xor
        
        for num in nums:
            if num & least_significant_bit:
                xor1 ^= num
            else:
                xor0 ^= num
        for i in range(1, n):
            if i & least_significant_bit:
                xor1 ^= i
            else:
                xor0 ^= i
        
        for num in nums:
            if num == xor0:
                return xor0, xor1
        
        return xor1, xor0

