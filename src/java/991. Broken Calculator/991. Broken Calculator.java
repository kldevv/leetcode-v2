class Solution {
    public int brokenCalc(int startValue, int target) {
        int count = 0;
        
        while (target > startValue) {
            count += 1;
            if (target % 2 == 1) {
                count += 1;
                target += 1;
            } 
            target /= 2;
        }
        
        return count + (startValue - target);
    }
}