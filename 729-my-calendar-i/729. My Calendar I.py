class MyCalendar:

    # do not assume that the next interval could NOT be larger than the current one
    # i.e. [10, 25], next is [5, 30]
    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        lo, hi = 0, len(self.calendar)-1
        if len(self.calendar) == 0:
            self.calendar.insert(0, [start, end])
            return True
        ans = -1

        def isIntersect(mid, start, end):
            # example of how to use multi-optional return statement
            return (
                (self.calendar[mid][1] > start) or
                (self.calendar[mid+1][0] < end and start < self.calendar[mid+1][1] if mid+1 < len(self.calendar) else False)
            )
        while lo <= hi:
            mid = lo + (hi - lo)//2

            if self.calendar[mid][0] <= start:
                if not isIntersect(mid, start, end):
                    ans = mid+1 # only use the mid here
                    lo = mid + 1
                else:
                    return False
            else:
                hi = mid - 1
        
        if ans == -1:
            # check one more condition here 
            if self.calendar[0][0] < end:
                return False
            else:
                self.calendar.insert(0, [start, end])
        else:
            self.calendar.insert(ans, [start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)