class Solution:
    
    def originalDigits(self, s: str) -> str:
        c_counts = collections.Counter(s)
        
        result = [0] * 10
        
        # z only in zero
        result[0] = c_counts['z']
        # w only in two
        result[2] = c_counts['w']
        # u only in four
        result[4] = c_counts['u']
        # x only in six
        result[6] = c_counts['x']
        # g only in eight
        result[8] = c_counts['g']
        
        # s only in seven and six
        result[7] = c_counts['s'] - result[6]
        # f only in five and four
        result[5] = c_counts['f'] - result[4]
        # h only in three and eight
        result[3] = c_counts['h'] - result[8]
        # i in nine, five, six, and eight
        result[9] = c_counts['i'] - result[5] - result[6] - result[8]
        # o in one, zero, four, and two
        result[1] = c_counts['o'] - result[0] - result[4] - result[2]
        
        return "".join(str(num) * count for num, count in enumerate(result))
        
        
    