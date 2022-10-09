class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        cur_xor_mask = 0
        for i in range(len(pref)):
            pref[i] ^= cur_xor_mask
            cur_xor_mask ^= pref[i]
        return pref

