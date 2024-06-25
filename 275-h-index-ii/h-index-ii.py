class Solution:
    def hIndex(self, l: List[int]) -> int:
        c=0
        l.reverse()
        for i in range(len(l)):
            if l[i]>=i+1:
                c+=1
        return c