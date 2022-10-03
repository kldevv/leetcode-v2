class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)
        
        n = gcd(a, b)
        out = 0
        for i in range(1, int(sqrt(n))+1):
            if n % i == 0:
                if n // i == i:
                    out += 1
                else:
                    out += 2
        return out

