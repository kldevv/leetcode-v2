class Solution {
    public List<String> stringMatching(String[] words) {
        HashSet<String> matches = new HashSet<String>();
        
        int length = words.length;
        
        for (int i = 0; i < length; ++i) {
            String wordA = words[i];
            for (int j = i + 1; j < length; ++j) {
                String wordB = words[j];
                
                if (wordA.contains(wordB)) {
                    matches.add(wordB);
                }
                
                if (wordB.contains(wordA)) {
                    matches.add(wordA);
                }
            }
        }
        
        return new ArrayList<String>(matches);
    }
}