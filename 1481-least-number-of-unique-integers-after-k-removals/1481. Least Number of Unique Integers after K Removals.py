class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)

        cnt = [(v, k) for k, v in cnt.items()]

        cnt.sort()
        n = len(cnt)
        i = 0

        while k>=0 and i<n:
            if cnt[i][0] <= k:
                k -= cnt[i][0]
            else:
                k = 0
                break
            i += 1

        return n - i
            