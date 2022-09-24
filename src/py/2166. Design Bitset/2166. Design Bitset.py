class Bitset:

    def __init__(self, size: int):
        self.data = 0
        self.capacity = size
        self.size = 0

    def fix(self, idx: int) -> None:
        mask = 1 << idx
        if not self.data & mask:
            self.size += 1
            self.data |= mask

    def unfix(self, idx: int) -> None:
        mask = 1 << idx
        if self.data & mask:
            self.size -= 1
            self.data &= ~mask

    def flip(self) -> None:
        self.size = self.capacity - self.size
        self.data = ~self.data
        
    def all(self) -> bool:
        return self.size == self.capacity

    def one(self) -> bool:
        return self.size > 0

    def count(self) -> int:
        return self.size
        
    def toString(self) -> str:
        out = []
        for i in range(self.capacity):
            out.append(str(int(self.data & (1 << i) > 0)))
        return "".join(out)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()