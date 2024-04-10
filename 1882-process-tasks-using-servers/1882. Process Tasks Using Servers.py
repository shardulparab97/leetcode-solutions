class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(tasks)
        ans = [None] * n

        available = [(s, i) for i, s in enumerate(servers)]
        heapq.heapify(available)

        busy = []

        t = 0
    
        for i, task_time in enumerate(tasks):
            t = max(t, i)

            if len(available) == 0:
                t = busy[0][0]
            while busy and t>=busy[0][0]:
                t, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)
            ans[i] = index
            heapq.heappush(busy, (t + task_time, weight, index))

        return ans