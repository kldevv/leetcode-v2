class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = int(10 ** 9 + 7)
        
        arr.sort()        
        num_to_idx = {x: i for i, x in enumerate(arr)}
    
        dp = [1] * len(arr)
        for i, num in enumerate(arr):
            for left in range(i):
                # some element in the array is the right factor of num
                if num % arr[left] == 0 and num // arr[left] in num_to_idx:
                    right = num_to_idx[num // arr[left]]
                    dp[i] = (dp[i] + dp[left] * dp[right]) % MOD
        return sum(dp) % MOD

