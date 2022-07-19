class Solution {
    public int countOdds(int low, int high) {
        /**
        * Count number of odds for high(inclusive) and low(exclusive)
        */
        return (high + 1) / 2 - low / 2;
    }
}