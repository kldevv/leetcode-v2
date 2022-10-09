class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longest_task_dur = logs[0][1]
        out_id = logs[0][0]
        for i, (id_, leave_time) in enumerate(logs):
            if i > 0:
                pre_leave_time = logs[i-1][1]
                task_dur = leave_time - pre_leave_time
                if task_dur > longest_task_dur or task_dur == longest_task_dur and id_ < out_id:
                    out_id = id_
                    longest_task_dur = task_dur
        return out_id

