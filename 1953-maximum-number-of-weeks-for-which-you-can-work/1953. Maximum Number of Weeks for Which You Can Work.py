class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx = max(milestones)
        s = sum(milestones)
        s1 = s - mx

        # print(s, s1, mx)

        if mx <= s1:
            return s
        return 2*s1 + 1