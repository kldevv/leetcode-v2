class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1
        start2, end2 = event2
        if start1 < start2 and end1 < start2 or start1 > start2 and end2 < start1:
            return False
        return True

