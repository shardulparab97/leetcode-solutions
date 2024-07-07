class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        total_bottles = numBottles
        while total_bottles >= numExchange:
            remainingBottles = total_bottles%numExchange
            newBottles = total_bottles//numExchange
            ans += newBottles
            total_bottles = newBottles +  remainingBottles

        return ans