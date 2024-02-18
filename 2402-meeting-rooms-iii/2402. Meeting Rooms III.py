class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        len_meetings = len(meetings)
        meetings_dict =  [0] * n
        unused = [i for i in range(n)]
        used = []

        for i in range(len_meetings):
            while used and used[0][0] <= meetings[i][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(unused, room)
            
            if unused:
                room = heapq.heappop(unused)
                heapq.heappush(used, (meetings[i][1], room))
            else:
                used_end, room = heapq.heappop(used)
                heapq.heappush(used, (used_end + meetings[i][1]-meetings[i][0], room))
            
            meetings_dict[room] += 1

        # print(meetings_dict)
        return meetings_dict.index(max(meetings_dict))