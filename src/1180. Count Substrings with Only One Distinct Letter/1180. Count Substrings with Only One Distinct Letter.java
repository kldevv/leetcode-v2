class Solution {
    public int countLetters(String s) {
        int num = 0;
        int consecutiveLen = 1;
        
        for (int i = 1; i <= s.length(); ++i) {
            if (i == s.length() || s.charAt(i) != s.charAt(i-1)) {
                num += (1 + consecutiveLen) * consecutiveLen / 2;
                consecutiveLen = 1;
            }
            else {
                consecutiveLen += 1;
            }
        }
        
        return num;
    }
}