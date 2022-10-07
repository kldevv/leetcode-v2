class Solution:
    def checkValidString(self, s: str) -> bool:
        # low and high range of all the possible nest_level
        nest_level_range = [0, 0]
        for c in s:
            # lo (treat all *s as ")")
            nest_level_range[0] += 1 if c == "(" else -1
            # if lo < 0, we can treat some * as empty string
            nest_level_range[0] = max(nest_level_range[0], 0)
            # hi (treat all *s as "(")
            nest_level_range[1] += 1 if c != ")" else -1
            # some close brackets is not match even when we treat all *s as "("
            if nest_level_range[1] < 0:
                return False
        # some open brackets is not close even when we treat all *s as ")"
        return nest_level_range[0] == 0

