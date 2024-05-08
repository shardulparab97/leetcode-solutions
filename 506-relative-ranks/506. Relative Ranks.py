class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [None] * n
        score = [(s, i) for i, s in enumerate(score)]

        score.sort(reverse=True)

        for i, s in enumerate(score):
            sc, idx = s
            if i == 0:
                ans[idx] = 'Gold Medal'
            elif i == 1:
                ans[idx] = 'Silver Medal'
            elif i == 2:
                ans[idx] = 'Bronze Medal'
            else:
                ans[idx] = str(i+1)

        return ans