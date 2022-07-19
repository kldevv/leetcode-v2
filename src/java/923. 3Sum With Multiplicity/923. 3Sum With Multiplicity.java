class Solution {
    public int threeSumMulti(int[] arr, int target) {
        final int MOD = (int) Math.pow(10, 9) + 7;
        
        int n = arr.length;

        Map<Integer, Integer> offsetCounts = new HashMap<>();
        
        int result = 0;
        
        for (int i = 0; i + 2 < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                Integer offset = target - arr[i] - arr[j];
                
                if (offsetCounts.containsKey(offset)) {
                    result += offsetCounts.get(offset) % MOD;
                    result %= MOD;
                }
                
                offsetCounts.put(arr[j], offsetCounts.getOrDefault(arr[j], 0) + 1);
            }
            offsetCounts.clear();
        }
        
        return result;
    }
}