class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        num_rooms = 0
        ans = -1

        times = []
        for i in intervals:
                times.append((i[0], 1))
                times.append((i[1], -1))
        
        times.sort()

        for t in times:
            num_rooms += t[1]
            ans = max(ans, num_rooms)

        return ans
