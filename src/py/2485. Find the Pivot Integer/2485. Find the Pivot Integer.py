class Solution:
    def pivotInteger(self, n: int) -> int:
#         all_sum = (n+1) * n // 2
        
#         first_h_sum = (x+1) * x // 2
#         second_h_sum = all_sum - ((x-1) * x // 2)
        
#         x = sqrt((n+1)*n // 2)
        
        k = (n+1) * n
        if k % 2 or isqrt(k // 2) ** 2 != k // 2:
            return -1
        return isqrt(k // 2)
        