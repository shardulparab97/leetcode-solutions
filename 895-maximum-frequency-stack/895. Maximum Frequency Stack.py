class FreqStack:

    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.group = collections.defaultdict(list)
        self.maxFreq = float("-inf")
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
        
        
    def pop(self) -> int:
        res = self.group[self.maxFreq].pop()
        self.freq[res] -= 1
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1
        
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()