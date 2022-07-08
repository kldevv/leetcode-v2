class Solution {
    public boolean isPathCrossing(String path) {
        HashSet<String> visited = new HashSet<String>();
        visited.add("0,0");
        
        int r = 0;
        int c = 0;
        
        for (int i = 0; i < path.length(); ++i) {
            char direction = path.charAt(i);
            switch (direction) {
                case 'N':
                    r += 1;
                    break;
                case 'S':
                    r -= 1;
                    break;
                case 'E':
                    c += 1;
                    break;
                case 'W':
                    c -= 1;
                    break;
            }
            
            String point = String.valueOf(r) + "," + String.valueOf(c);
            if (visited.contains(point)) {
                return true;
            }
            visited.add(point);
        }
        
        return false;
    }
}