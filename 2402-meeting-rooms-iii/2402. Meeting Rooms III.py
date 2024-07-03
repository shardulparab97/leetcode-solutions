class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        used = []
        unused = [i for i in range(n)]

        meetings_dict = [0] * n

        for m in meetings:
            st, en = m
            while used and used[0][0] <= st:
                _, room_number = heapq.heappop(used)
                heapq.heappush(unused, room_number)
            if unused: # soom rooms available
                room_number = heapq.heappop(unused)
                heapq.heappush(used, (en, room_number))
            else:
                end_time, room_number = heapq.heappop(used)
                heapq.heappush(used, (end_time + en - st, room_number))
            meetings_dict[room_number] += 1

        print(meetings_dict)
        return meetings_dict.index(max(meetings_dict))