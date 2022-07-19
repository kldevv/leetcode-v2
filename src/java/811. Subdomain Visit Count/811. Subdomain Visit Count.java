class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> counts = new HashMap();
        
        for (var cpdomain : cpdomains) {
            String[] countAndDomain = cpdomain.split(" ");
            
            Integer count = Integer.valueOf(countAndDomain[0]);
            String[] domains = countAndDomain[1].split("\\.");
            
            String domain = "";
            for (int i = domains.length - 1; i >= 0; --i) {
                if (domain.length() > 0) {
                    domain = domains[i] + "." + domain;   
                }
                else {
                    domain = domains[i] + domain;
                }
                counts.put(domain, counts.getOrDefault(domain, 0) + count);
            }
        }
        
        List<String> outputs = new ArrayList<String>();
        for (var set : counts.entrySet()) {
            outputs.add(set.getValue() + " " + set.getKey());
        }
        
        return outputs;
    }
}