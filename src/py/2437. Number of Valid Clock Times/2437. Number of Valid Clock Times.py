class Solution:
    def countTime(self, time: str) -> int:
        hour, minute = time.split(":")
        
        out = 1
        if hour[0] == hour[1] == "?":
            out *= 24
        else:
            if hour[0] == "?":
                if int(hour[1]) > 3:
                    out *= 2
                else:
                    out *= 3
            if hour[1] == "?":
                if int(hour[0]) == 2:
                    out *= 4
                else:
                    out *= 10
        
        if minute[0] == minute[1] == "?":
            out *= 60
        else:
            if minute[0] == "?":
                out *= 6
            if minute[1] == "?":
                out *= 10
        
        return out