class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # count occurrence of elements
        out = 0
        n = len(arr)
        for i, num in enumerate(arr):
            left_subarray_cnt = i
            left_even_subarray_cnt = (left_subarray_cnt // 2 + 1)
            left_odd_subarray_cnt = (left_subarray_cnt + 1) // 2
            
            right_subarray_cnt = n - i - 1
            right_even_subarray_cnt = (right_subarray_cnt // 2 + 1)
            right_odd_subarray_cnt = (right_subarray_cnt + 1) // 2
            
            out += num * (left_even_subarray_cnt*right_even_subarray_cnt + left_odd_subarray_cnt*right_odd_subarray_cnt)
            
        return out