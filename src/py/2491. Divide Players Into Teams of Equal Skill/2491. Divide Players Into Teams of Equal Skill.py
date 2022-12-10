class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        eq_skill = sum(skill) * 2 // len(skill)
        skills = Counter(skill)

        out = 0
        for s, c in skills.items():
            # if the occurrence of s and its pair not equal, impossible to yield valid answer
            if skills[s] != skills[eq_skill - s]:
                return -1
            out += skills[s] * s * (eq_skill-s)
        
        # correct for double counting
        return out // 2 