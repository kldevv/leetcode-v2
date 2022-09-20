class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        cpid = collections.defaultdict(list)
        for id_, p in zip(pid, ppid):
            cpid[p].append(id_)
        
        out = [kill]
        for id_ in out:
            for cp in cpid[id_]:
                out.append(cp)
        
        return out

