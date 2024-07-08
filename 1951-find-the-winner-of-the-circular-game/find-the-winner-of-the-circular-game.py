class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x=list(range(1,n+1))
        i = 0
        while len(x)>1:
            r=(i+k-1)%len(x)
            x.pop(r)
            i=r
        return x[0]
            
