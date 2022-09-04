class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # memo first position
        
        ALPHA_COUNT = 26
        FIRST_CHAR_CODE = ord('a')
        
        first_pos = [None] * ALPHA_COUNT
        
        for i, c in enumerate(s):
            slot = ord(c) - FIRST_CHAR_CODE
            if first_pos[slot] is not None:
                if distance[slot] != i - first_pos[slot] - 1:
                    return False
            else:
                first_pos[slot] = i
                
        return True
