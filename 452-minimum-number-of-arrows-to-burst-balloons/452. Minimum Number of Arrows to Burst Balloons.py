class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        n = len(points)
        points.sort()
        curr_idx = 0
        curr_s, curr_e = points[0][0], points[0][1]
        for i in range(1, n):
            ps, pe = points[i]
            if not(ps<=curr_e and curr_s<=pe):
                ans += 1
                curr_s, curr_e = ps, pe
            else:
                curr_s = max(curr_s, ps)
                curr_e = min(curr_e, pe)

        return ans
               

