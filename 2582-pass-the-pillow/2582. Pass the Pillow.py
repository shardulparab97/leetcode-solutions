class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num_passes = n-1
        if time // num_passes % 2 == 1:
            return n - (time % num_passes)
        else:
            return (time%num_passes) + 1
        
        

