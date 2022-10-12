class TimeMap:
    def __init__(self):
        self.storage = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        i = bisect.bisect(self.storage[key], timestamp, key=lambda x:x[0])
        return self.storage[key][i-1][1] if i else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)