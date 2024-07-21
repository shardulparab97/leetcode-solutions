class OrderedStream:

    def __init__(self, n: int):
        self.mp = {}
        self.curr_ptr = 1


    def insert(self, idKey: int, value: str) -> List[str]:
        self.mp[idKey] = value
        ans = []
        if self.curr_ptr == idKey:
            while self.curr_ptr in self.mp: 
                ans.append(self.mp[self.curr_ptr])
                del self.mp[self.curr_ptr]
                self.curr_ptr += 1
        return ans

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)