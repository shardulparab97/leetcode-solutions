class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        pq = []
        data = []

        for idx, (a, d) in enumerate(zip(apples, days)):
            data.append((idx+d-1, a))

        ans = 0
        # storing for the first few days
        # data already sorted
        for i in range(n):
            if data[i][1] > 0:
                heapq.heappush(pq, data[i])
            
            # one more mistake we loop till we find one case which is useful
            # else throw out 
            while pq:
                en, a = heapq.heappop(pq)
                if en >= i:
                    ans += 1
                    a -= 1
                    if a != 0:
                        heapq.heappush(pq, (en, a))
                    break

        # now we have stored all the data --> now for the remaining days
        i += 1 # for loops i stops at n-1

        # two conditions
        # keep on looping till we find a day which can be useful, then move onto the next day
        while pq:
                en, a = heapq.heappop(pq)
                if en >= i:
                    ans += 1
                    a -= 1
                    if a != 0:
                        heapq.heappush(pq, (en, a))
                    i+= 1
            

        return ans
            

                



        