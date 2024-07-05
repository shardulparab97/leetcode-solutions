class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort(reverse = True)
        sm = sum(milestones[1:])

        if milestones[0] <= sm:
            return sum(milestones)
        return 2*sm + 1