class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        times = {v:0 for v in tasks} # store the ending time for each task's previous occurrence
        curr_time = 0
        for task in tasks:
            if times[task] > curr_time:
                # wait for the cooldown time to happen
                curr_time = times[task]
            curr_time += 1
            times[task] = curr_time+space
        return curr_time