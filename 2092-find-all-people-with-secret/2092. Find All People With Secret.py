class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = [[] for _ in range(n)]

        for m in meetings:
            g[m[0]].append((m[1], m[2]))
            g[m[1]].append((m[0], m[2]))

        q = collections.deque()

        earliest = [float("inf")] * n
        earliest[0] = 0
        earliest[firstPerson] = 0
        q.append((0, 0))
        q.append((firstPerson, 0))

        while q:
            person, time = q.popleft()

            for secondPerson, meetingTime in g[person]:
                if meetingTime >= time and earliest[secondPerson] > meetingTime:
                    q.append((secondPerson, meetingTime))
                    earliest[secondPerson] = meetingTime

        return [i for i,_ in enumerate(earliest) if earliest[i] != float("inf")]

        

