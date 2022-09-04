class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # T(n): nlog(n), S(n): log(n)
        # priority queue
        
        meetings.sort()
        
        # end_time, room_num
        ongoing = []
        # room_num
        ava_room = [i for i in range(n)]
        use_counts = [0] * n
    
        for start, end in meetings:
            # see if there are new available rooms
            while ongoing and ongoing[0][0] <= start:
                last_end, room_num = heapq.heappop(ongoing)
                heapq.heappush(ava_room, room_num)
            # use the now available, otherwise delay meeting
            if ava_room:
                room_num = heapq.heappop(ava_room)
                heapq.heappush(ongoing, (end, room_num))
            else:
                last_end, room_num = heapq.heappop(ongoing)
                heapq.heappush(ongoing, (last_end + end - start, room_num))
            
            use_counts[room_num] += 1
        
        return use_counts.index(max(use_counts))