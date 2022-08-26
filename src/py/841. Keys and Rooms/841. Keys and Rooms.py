class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:             
        unlocked_rooms = [False] * len(rooms)
        unlocked_rooms[0] = True
        q = [0]
        
        while q:
            room = q.pop()
            for unlock_room in rooms[room]:
                if not unlocked_rooms[unlock_room]:
                    unlocked_rooms[unlock_room] = True
                    q.append(unlock_room)
        
        return all(unlocked_rooms)
