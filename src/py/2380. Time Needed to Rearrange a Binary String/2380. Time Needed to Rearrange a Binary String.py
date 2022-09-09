class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # dp
        # keep track of the minimum seconds required for i-th if i-th is 1
        zero_count = 0
        min_second_required = 0
        
        for i, c in enumerate(s):
            zero_count += (c == '0')
            if c == '1' and zero_count:
                # for every 1, we need at least zero_count seconds
                # and if (i-1)-th is 1, we need extra one second on (i-1)-th's minimum required second (wait for (i-1) to move to the right position)
                min_second_required = max(min_second_required + 1, zero_count)
        
        return min_second_required

