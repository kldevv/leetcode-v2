class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int ns = s.length();
        int np = p.length();
        
        int[] pCounts = new int[26];
        for (var c : p.toCharArray()) {
            pCounts[c - 'a'] += 1;
        }
        
        List<Integer> outputs = new ArrayList<Integer>();
        int[] sCounts = new int[26]; 
        
        for (int i = 0; i < ns; ++i) {
            sCounts[s.charAt(i) - 'a'] += 1;
            
            if (i >= np) {
                sCounts[s.charAt(i - np) - 'a'] -= 1;
            }
            
            if (Arrays.equals(sCounts, pCounts)) {
                outputs.add(i - np + 1);
            }
        }
        
        return outputs;
    }
}