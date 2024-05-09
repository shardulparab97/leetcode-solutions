class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0

        for turn in range(k):
            ans += max(happiness[turn] - turn, 0)

        return ans
