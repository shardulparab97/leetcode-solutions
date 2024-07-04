class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        ans = [[intervals[0][0], intervals[0][1]]]

        for l,r in intervals[1:]:
            if ans[-1][0] <= l and r<=ans[-1][1]:
                continue
            else:
                ans.append([l, r])

        return len(ans)


