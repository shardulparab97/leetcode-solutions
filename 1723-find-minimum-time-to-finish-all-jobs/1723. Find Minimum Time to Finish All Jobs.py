class Solution:    
    def minimumTimeRequired(self, jobs: List[int], num_workers: int) -> int:
        n = len(jobs)
        worker_cost = [0] * (1 << n)
        for state in range(1 << n):
            for i in range(n):
                if state & (1 << i):
                    worker_cost[state] += jobs[i]
                    
        @functools.cache
        def compute_time(state: int, curr_workers: int) -> int:
            if curr_workers == 1:
                return worker_cost[state]
            
            best = float("inf")
            worker_state = state
            while worker_state:
                if worker_cost[worker_state] < best:
                    best = min(best, max(compute_time(state ^ worker_state, curr_workers - 1), worker_cost[worker_state]))
                worker_state = (worker_state - 1) & state
            
            return best
            
        return compute_time((1 << n) - 1, num_workers)