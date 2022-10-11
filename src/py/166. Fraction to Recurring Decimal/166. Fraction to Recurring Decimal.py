class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # if the result is negative, cache the sign and reapply
        if numerator * denominator < 0:
            return "-" + self.fractionToDecimal(abs(numerator), abs(denominator))
            
        digit = str(numerator // denominator)
        numerator = (numerator % denominator) * 10
        decimals = []
        reoccur_numerator = {}
        while numerator:
            if numerator in reoccur_numerator:
                reoccur_start = reoccur_numerator[numerator]
                reoccur = "".join(decimals[reoccur_start:])
                non_reoccur = "".join(decimals[:reoccur_start])
                return f"{digit}.{non_reoccur}({reoccur})"
            decimals.append(str(numerator // denominator))
            reoccur_numerator[numerator] = len(decimals) - 1
            numerator = (numerator % denominator) * 10
        
        if decimals:
            non_reoccur = "".join(decimals)
            return f"{digit}.{non_reoccur}"
        return digit

