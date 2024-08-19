class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        c=0
        f=2
        while n>1:
            while n%f==0:
                c+=f
                n//=f
            f+=1
        return c