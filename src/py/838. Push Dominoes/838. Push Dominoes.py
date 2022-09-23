class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        force = 0
        for i in range(n):
            if dominoes[i] == "R":
                force = n
            if dominoes[i] == "L":
                force = 0
            if dominoes[i] == ".":
                force -= 1
            forces[i] = max(0, force)
        
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                force = -n
            if dominoes[i] == "R":
                force = 0
            if dominoes[i] == ".":
                force += 1
            forces[i] += min(0, force)
        
        out = []
        for f in forces:
            if f > 0:
                out.append("R")
            elif f < 0:
                out.append("L")
            else:
                out.append(".")
        return "".join(out)
        