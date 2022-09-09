class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        cur_white_count = 0
        min_white_count = n
        
        for end in range(n):
            cur_white_count += (blocks[end] == 'W')
            if end >= k:
                cur_white_count -= (blocks[end - k] == 'W')
            
            # record minimum white count in the sliding window
            if end >= k-1:
                min_white_count = min(cur_white_count, min_white_count)
                
        return min_white_count

