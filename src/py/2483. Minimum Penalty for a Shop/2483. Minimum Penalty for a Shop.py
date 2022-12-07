class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        cur_score = 0
        max_score = 0
        out = 0
        for i in range(n+1):
            if cur_score > max_score:
                out = i
                max_score = cur_score
            # accum the Y and N encountered
            # to max Y and min N, where weight(Y) == weight(N)
            if i < n:
                cur_score += 1 if customers[i] == "Y" else -1
        return out
  