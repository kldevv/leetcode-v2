class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # iterate through the possible combination and collect ones with the right bit count
        return [f"{h}:{m if m >= 10 else '0'+ str(m)}" for h in range(12) for m in range(60) if (bin(m) + bin(h)).count("1") == turnedOn]