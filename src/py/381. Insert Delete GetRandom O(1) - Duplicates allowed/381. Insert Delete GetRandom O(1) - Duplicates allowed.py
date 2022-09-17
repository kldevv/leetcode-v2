class RandomizedCollection:

    def __init__(self):
        self.data = []
        self.pos = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        self.pos[val].append(len(self.data))
        self.data.append((val, len(self.pos[val])-1))
        return len(self.pos[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        last_val, last_val_pos = self.data[-1]
        self.pos[last_val][last_val_pos] = self.pos[val][-1]
        self.data[self.pos[val][-1]] = (last_val, last_val_pos)
        self.data.pop()
        self.pos[val].pop()
        if not self.pos[val]:
            del self.pos[val]
        return True
        
    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data)-1)][0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()