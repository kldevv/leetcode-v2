class Solution:
    def addDigits(self, num: int) -> int:
        # digital root
        # the digital root is continous incrementing by 1 from 1
        # and wrap around when reach 9
        # 0 is special case
        return 0 if num == 0 else (num-1) % 9 + 1

