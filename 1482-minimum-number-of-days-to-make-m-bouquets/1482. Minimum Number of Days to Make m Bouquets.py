class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = -1

        lo, hi = 0, 1e9
        len_bd = len(bloomDay)

        def check_bouquets(days, m, k):
            # find how many adjacent flower options are there
            res = 0
            st, en = 0, 0
            curr_cnt = 0
            while en < len_bd:
                bd = bloomDay[en]
                if bd <= days:
                    curr_cnt += 1
                else:
                    curr_cnt = 0
                if curr_cnt == k:
                    res += 1
                    curr_cnt = 0
                en += 1

            if res >= m:
                return True
            return False

            

        while lo <= hi:
            mid = lo + (hi - lo)//2

            if check_bouquets(mid, m, k):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return int(ans)