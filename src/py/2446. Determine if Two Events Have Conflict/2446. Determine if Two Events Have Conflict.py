class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def to_second(time):
            hour, minute = time.split(":")
            return int(hour) * 60 + int(minute)
        
        start1, end1 = list(map(to_second, event1))
        start2, end2 = list(map(to_second, event2))
        if start1 < start2 and end1 < start2 or start1 > start2 and end2 < start1:
            return False
        return True

