class Solution {
    public int sumSubarrayMins(int[] arr) {
        final int MOD = (int) Math.pow(10, 9) + 7;
        
        int n = arr.length;
        long[] left = new long[n];
        
        Stack<Integer> ple = new Stack();
        for (int i = 0; i < n; ++i) {
            while (!ple.empty() && arr[i] < arr[ple.peek()] ) {
                ple.pop();
            }
            left[i] = (ple.empty() ? -1 : ple.peek());
            ple.push(i);
        }
        
        Stack<Integer> nle = new Stack();
        long[] right = new long[n];
        
        for (int i = n - 1; i >= 0; --i) {
            while (!nle.empty() && arr[i] <= arr[nle.peek()]) {
                nle.pop();
            }
            right[i] = (nle.empty() ? n : nle.peek());
            nle.push(i);
        }
        
        long result = 0;
        for (int i = 0; i < n; i++)  {
            result += (
                arr[i] % MOD
                * (i - left[i]) % MOD
                * (right[i] - i) % MOD
            ) % MOD;
            result %= MOD;
        }
        
        return (int) result;
    }
}