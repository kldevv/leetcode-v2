class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        if alice_sum > bob_sum:
            return list(reversed(self.fairCandySwap(bobSizes, aliceSizes)))
        
        target = (alice_sum + bob_sum) // 2
        alice_need = target - alice_sum
        
        bob_set = set(bobSizes)
        for n in aliceSizes:
            if alice_need + n in bob_set:
                return (n, alice_need + n)
            