class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l=len(rolls)
        t=mean*(n+l)
        s=sum(rolls)
        m=t-s
        if m<n or m>6*n:
            return []
        b=m//n
        r=m%n
        ans=[b]*n
        for i in range(r):
            ans[i]+=1
        return ans
