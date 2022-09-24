class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_digit_count = len(str(low))
        high_digit_count = len(str(high))
        
        out = []
        for digit_count in range(low_digit_count, high_digit_count+1):
            for start in range(1, 10-digit_count+1):
                num = int("".join([str(start+i) for i in range(digit_count)]))
                if num < low:
                    continue
                if num > high:
                    break
                out.append(num) 
        return out

