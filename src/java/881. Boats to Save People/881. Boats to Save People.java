class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        
        int count = 0;
        int i = 0;
        int j = people.length - 1;
        
        while (i <= j) {
            count += 1;
            if (people[i] + people[j] <= limit) {
                i += 1;
            }
            j -= 1;
        }
        
        return count;
    }
}