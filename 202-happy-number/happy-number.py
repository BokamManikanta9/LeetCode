class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n))>1:
            s=0
            for i in str(n):
                s+=int(i)**2
            n=s
        if n==1 or n==7:
            return True
        else:
            return False
        