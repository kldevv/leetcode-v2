class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        
        max_even_num = -1
        max_even_count = -1
        
        for num, count in counts.items():
            if num % 2 == 0:
                if count > max_even_count or count == max_even_count and num < max_even_num:
                    max_even_count = count
                    max_even_num = num
            
        return max_even_num