class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bit_cnt = num1.bit_count()
        num2_bit_cnt = num2.bit_count()
        
        out = num1
        for i in range(32):
            mask = 1 << i
            if num1_bit_cnt > num2_bit_cnt and num1 & mask > 0:
                out ^= mask
                num1_bit_cnt -= 1
        
            if num1_bit_cnt < num2_bit_cnt and num1 & mask == 0:
                out ^= mask
                num1_bit_cnt += 1
        return out

