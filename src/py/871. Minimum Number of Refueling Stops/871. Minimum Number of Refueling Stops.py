class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur_pos = 0
        cur_fuel = startFuel
        
        stops = 0
        cand_stops = []
        stations.append((target, 0))
        for pos, fuel in stations:
            cur_fuel -= pos - cur_pos
            while cand_stops and cur_fuel < 0:
                cur_fuel -= heapq.heappop(cand_stops)
                stops += 1
            if cur_fuel < 0:
                return -1
            heapq.heappush(cand_stops, -fuel)
            cur_pos = pos
        return stops

