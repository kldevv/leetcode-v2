public class Solution {
    public String[] findRelativeRanks(int[] score) {
        Integer[] index = new Integer[score.length];
        for (int i = 0; i < index.length; ++i) {
            index[i] = Integer.valueOf(i);
        }
        
        Arrays.sort(index, (a, b) -> (Integer.compare(score[b], score[a])));
        
        String[] result = new String[score.length];
        for (int i = 0; i < result.length; ++i) {
            if (i == 0) {
                result[index[i]] = "Gold Medal";
            }
            else if (i == 1) {
                result[index[i]] = "Silver Medal";
            }
            else if (i == 2) {
                result[index[i]] = "Bronze Medal";
            }
            else {
                result[index[i]] = String.valueOf(i + 1);
            }
        }
        return result;
    }
}