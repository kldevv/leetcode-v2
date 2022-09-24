class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        thousand_translation = ["Thousand", "Million", "Billion"]
        small_translation = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        big_translation = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        out = []
        
        def parse(num, i):
            nonlocal out
            
            if not num:
                return
            
            parse(num // 1000, i+1)
            
            digits = num % 1000
            if digits:
                if digits >= 100:
                    out.append(small_translation[digits // 100])
                    out.append("Hundred")
                if digits % 100:
                    digits %= 100
                    if digits < 20:
                        out.append(small_translation[digits])
                    else:
                        out.append(big_translation[digits // 10])
                        if digits % 10:
                            out.append(small_translation[digits % 10])
            if i and digits:
                out.append(thousand_translation[i-1])
            
        
        parse(num, 0)
        return " ".join(out)
            
            
            