class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # n = len(apples)
        # pq = []
        # data = []

        # for idx, (a, d) in enumerate(zip(apples, days)):
        #     data.append((idx+d-1, a))

        # ans = 0
        # # storing for the first few days
        # # data already sorted
        # for i in range(n):
        #     if data[i][1] > 0:
        #         heapq.heappush(pq, data[i])
            
        #     # one more mistake we loop till we find one case which is useful
        #     # else throw out 
        #     while pq:
        #         en, a = heapq.heappop(pq)
        #         if en >= i:
        #             ans += 1
        #             a -= 1
        #             if a != 0:
        #                 heapq.heappush(pq, (en, a))
        #             break

        # # now we have stored all the data --> now for the remaining days
        # i += 1 # for loops i stops at n-1

        # # two conditions
        # # keep on looping till we find a day which can be useful, then move onto the next day
        # while pq:
        #         en, a = heapq.heappop(pq)
        #         if en >= i:
        #             ans += 1
        #             a -= 1
        #             if a != 0:
        #                 heapq.heappush(pq, (en, a))
        #             i+= 1
            

        # return ans
        A = apples
        D = days
        ans, i, N = 0, 0, len(A)
        h = []
        while i < N or h:
            # only push to heap when you have a valid i, and the apple has atleast one day to stay fresh.
            if i<N and A[i] > 0:
                heapq.heappush(h, [i+D[i], A[i]])
            # remove the rotten apples batches and the batches with no apples left (which might have got consumed).
            while h and (h[0][0] <= i or h[0][1] <= 0):
                heapq.heappop(h)
            # only if there is batch in heap after removing all the rotten ones, you can eat. else wait for the subsequent days for new apple batch by incrementing i.
            if h:
                h[0][1]-=1
                ans+=1
            i+=1
        return ans 
            

                



        