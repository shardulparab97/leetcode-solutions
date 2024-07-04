"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

# class Solution:
#     def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
#         # main issue with saving them all in one big list is if 
#         # there is a limit on the compile

#         # So we use heaps for a nlogk Solution
#         n = len(schedule)
#         pq = []
#         for sched in schedule[0]:
#             heapq.heappush(pq, (sched.start, sched.end))


#         for i in range(1, n):
#             sched_list = schedule[i]
            

            
#             for sched in sched_list:
#                 vis = []
#                 res = (sched.start, sched.end)
#                 while pq:
#                     prev_start, prev_end = heapq.heappop(pq)
#                     if sched.start <= prev_end and prev_start <= sched.end: # there is an overlap
#                         new_start = min(prev_start, sched.start)
#                         new_end = max(prev_end, sched.end)

#                         heapq.heappush(pq, (new_start, new_end))

#                         break
#                     else:
#                         # heapq.heappush(pq, (sched.start, new_end))
#                         vis.append((prev_start, prev_end))
            
#                 if not pq:
#                     heapq.heappush(pq, (sched.start, sched.end))
#                 for v in vis:
#                     heapq.heappush(pq, (v[0], v[1]))
            
#         ans = []
#         # lo = 1

#         # print(pq)
#         # print(pq)

#         # do one final merge
#         # pq = [(0, 26), (39, 87), (27, 36), (91, 99), (61, 75), (78, 81)]
#         # heapq.heapify(pq)
#         # print(pq)

        

#         # res = [heapq.heappop(pq)]
#         # while pq:
#         #     prev_start, prev_end = res[-1]
#         #     curr_start, curr_end = heapq.heappop(pq)
#         #     if prev_start <= curr_end and curr_start <= prev_end:
#         #         curr_start = min(prev_start, curr_start)
#         #         curr_end = max(prev_end, curr_end)
#         #     if (prev_start, prev_end) != (curr_start, curr_end):
#         #         res.append([curr_start, curr_end])
            
#         # # print(res)
                

#         # ans = []
#         # for i in range(1, len(res)):
#         #     ans.append(Interval(res[i-1][1], res[i][0]))


#         # return ans
#         # instead do a simple sort
#         ans = []
#         pq.sort()
#         print(pq)
#         # print(len(pq))
#         for i in range(1, len(pq)):
#             # print(i)
#             ans.append(Interval(pq[i-1][1], pq[i][0]))

#         return ans


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':        
        free_time_list = []
        min_start_heap = []
        
        # push all employees first event start time with their idx to a heap 
        
        # start time, emp_idx, event_idx
        for emp_idx, emp_schedule in enumerate(schedule):
            heapq.heappush(min_start_heap, (emp_schedule[0].start, emp_idx, 0))
        
        _, emp_idx, event_idx = min_start_heap[0]
        prev_end = schedule[emp_idx][event_idx].end
        
        
        # iterate heap
        while min_start_heap:            
            # emp_idx, start = pop next event
            start_time, emp_idx, event_idx = heapq.heappop(min_start_heap)
            
            # add next employee event to the heap
            if event_idx + 1 < len(schedule[emp_idx]):
                heapq.heappush(min_start_heap, (schedule[emp_idx][event_idx+1].start, emp_idx, event_idx+1))
            
            # if there's a gap between last end and current start, add prev end -> start interval
            if prev_end < start_time:
                free_time_list.append(Interval(start=prev_end, end=start_time))
                
            # update prev_end to the end of current shift
            prev_end = max(prev_end, schedule[emp_idx][event_idx].end)
                    
        # return list
        return free_time_list            
        