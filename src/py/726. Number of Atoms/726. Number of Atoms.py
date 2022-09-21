class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        def parse():
            nonlocal i
            counts = collections.defaultdict(int)
            while i < n and formula[i] != ")":
                if formula[i] == "(":
                    i += 1
                    for element, count in parse().items():
                        counts[element] += count
                else:
                    # parse element
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    element = formula[i_start:i]
                    # parse coef
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    coef = int(formula[i_start:i] or 1)
                    counts[element] += coef
            i += 1
            # parse coef
            i_start = i
            while i < n and formula[i].isdigit():
                i += 1
            if i > i_start:
                coef = int(formula[i_start:i] or 1)
                for element in counts.keys():
                    counts[element] *= coef
                    
            return counts

        counts = parse()
        out = []
        for element in sorted(counts.keys()):
            out.append(element)
            if counts[element] > 1:
                out.append(str(counts[element]))
        return "".join(out)
    