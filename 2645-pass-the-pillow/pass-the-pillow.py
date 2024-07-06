class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x=(n-1)*2
        y=time%x
        if y<n:
            return y+1
        else:
            return 2*n-y-1
