class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx = float("-inf")
        s = 0
        for m in milestones:
            if m > mx:
                mx = m
            s += m

        s1 = s - mx

        # print(s, s1, mx)

        if mx <= s1:
            return s
        return 2*s1 + 1