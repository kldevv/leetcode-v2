class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        p = {rc : r[0] for r in regions for rc in r[1:]}
        
        chain_to_root = set([region1])
        while region1 in p:
            region1 = p[region1]
            chain_to_root.add(region1)
            
        while region2 not in chain_to_root:
            region2 = p[region2]
        
        return region2
            