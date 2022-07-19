class UndergroundSystem {
    private Map<Integer, Integer> checkInTimes = new HashMap<>();
    private Map<Integer, String> checkInStationNames = new HashMap<>();
    /**
    * checkInStation/checkOutStation -> Avg
    */
    private Map<String, Integer> totals = new HashMap<>();
    private Map<String, Integer> counts = new HashMap<>();

    public UndergroundSystem() {
        
    }
    
    public void checkIn(int id, String stationName, int t) {
        checkInTimes.put(id, t);
        checkInStationNames.put(id, stationName);
    }
    
    public void checkOut(int id, String stationName, int t) {
        String key = checkInStationNames.get(id) + "/" + stationName;
        
        totals.put(
            key, totals.getOrDefault(key, 0) + (t - checkInTimes.get(id))
        );
        counts.put(
            key, counts.getOrDefault(key, 0) + 1
        );
        
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String key = startStation + "/" + endStation;
        
        return (double) totals.get(key) / counts.get(key);
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */