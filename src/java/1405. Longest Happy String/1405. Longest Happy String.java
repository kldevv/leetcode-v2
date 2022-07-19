class Solution {
    public String longestDiverseString(int a, int b, int c) {
        return longestDiverseString(a, b, c, "a", "b", "c");
    }
    
    public String longestDiverseString(int a, int b, int c, String aS, String bS, String cS) {
        if (a < b) {
            return longestDiverseString(b, a, c, bS, aS, cS);
        }
        
        if (b < c) {
            return longestDiverseString(a, c, b, aS, cS, bS);
        }
        
        if (b == 0) {
            return aS.repeat(Math.min(2, a));
        }
        
        int aCount = Math.min(2, a);
        int bCount = (a - aCount >= b) ? 1 : 0;
        
        return aS.repeat(aCount) + bS.repeat(bCount) + longestDiverseString(
            a - aCount,
            b - bCount,
            c,
            aS,
            bS,
            cS
        );
    }
}