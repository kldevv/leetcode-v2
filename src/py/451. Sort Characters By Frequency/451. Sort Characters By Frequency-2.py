class Solution:
    def frequencySort(self, s: str) -> str:
        # tc(n) = klogk + n
        counts = collections.Counter(s)
        
        freq_2_chars = collections.defaultdict(list)
        for char, count in counts.items():
            freq_2_chars[count].append(char)
        
        out = []
        # klogk, where k == len(freqs)
        freqs = sorted(list(set([count for count in counts.values()])), reverse=True)
        # n iterate over all chars
        for freq in freqs:
            for char in freq_2_chars[freq]:
                out.append(char * freq)
        return "".join(out)

