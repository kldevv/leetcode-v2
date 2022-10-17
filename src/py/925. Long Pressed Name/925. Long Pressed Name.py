class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            
            cnt_i = 1
            while i < len(name)-1 and name[i] == name[i+1]:
                cnt_i += 1
                i += 1
                
            cnt_j = 1
            while j < len(typed)-1 and typed[j] == typed[j+1]:
                cnt_j += 1
                j += 1
                
            if cnt_j < cnt_i:
                return False
            i += 1
            j += 1
        
        return i == len(name) and j == len(typed)

