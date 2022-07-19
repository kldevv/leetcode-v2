class FirstUnique {
    private Set<Integer> queue = new LinkedHashSet<>();
    private HashMap<Integer, Boolean> isUnique = new HashMap<>();
    
    public FirstUnique(int[] nums) {
        for (var num : nums) {
            this.add(num);
        }
    }
    
    public int showFirstUnique() {
        if (!queue.isEmpty()) {
           return queue.iterator().next();
        }
        return -1;
    }
    
    public void add(int value) {
        if (!isUnique.containsKey(value)) {
            queue.add(value);
            isUnique.put(value, true);
        }
        else if (isUnique.get(value)){
            isUnique.put(value, false);
            queue.remove(value);
        }
    }
}

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique obj = new FirstUnique(nums);
 * int param_1 = obj.showFirstUnique();
 * obj.add(value);
 */