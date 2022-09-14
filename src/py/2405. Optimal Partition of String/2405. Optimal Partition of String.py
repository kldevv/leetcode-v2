class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        char_set = set()
        substring_count = 1
        for c in s:
            if c in char_set:
                substring_count += 1
                char_set.clear()
            char_set.add(c)
        return substring_count
        