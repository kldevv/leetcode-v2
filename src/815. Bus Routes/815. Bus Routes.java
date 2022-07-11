class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        Map<Integer, Set<Integer>> busNumbers = new HashMap<>();
        
        for (int i = 0; i < routes.length; ++i) {
            for (var stop : routes[i]) {
                Set<Integer> busNumber = busNumbers.getOrDefault(stop, new HashSet<Integer>());
                busNumber.add(i);
                busNumbers.put(stop, busNumber);
            }
        }
        
        if (!busNumbers.containsKey(target)) {
            return -1;
        }
        
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(source);
        
        Set<Integer> visited = new HashSet<>();
        int result = 0;
        
        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; ++i) {
                var stop = queue.poll();
                if (stop == target) {
                    return result;
                }
                var busNumber = busNumbers.get(stop);
            
                for (var bus : busNumber) {
                    for (var nextStop : routes[bus]) {
                        if (!visited.contains(nextStop)) {
                            queue.add(nextStop);
                            visited.add(nextStop);
                        }
                    }
                }   
            }
            result += 1;
        }
        
        return -1;
    }
}