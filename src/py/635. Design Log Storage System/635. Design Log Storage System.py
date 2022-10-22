class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp.split(":")))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        truc = {"Year": 1, "Month": 2, "Day": 3, "Hour": 4, "Minute": 5, "Second": 6}[granularity]
        
        start = start.split(":")[:truc]
        end = end.split(":")[:truc]
        
        out = []
        for id_, timestamp in self.logs:
            if start <= timestamp[:truc] <= end:
                out.append(id_)
        return out


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)