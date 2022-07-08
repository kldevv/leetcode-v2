class Solution {
    public String removeVowels(String s) {
        String[] v = {"a", "e", "i", "o", "u"};
        Set<String> vowels = new HashSet<String>(Arrays.asList(v));
        
        
        String result = "";
        for (var c : s.toCharArray()) {
            if (!vowels.contains(String.valueOf(c))) {
                result += c;
            }
        }
        
        return result;
    }
}