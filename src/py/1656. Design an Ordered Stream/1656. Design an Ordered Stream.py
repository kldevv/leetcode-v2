class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.cur = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1] = value
        out = []
        while self.cur < len(self.data):
            if self.data[self.cur] is None:
                break
            out.append(self.data[self.cur])
            self.cur += 1
        return out


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)