class Solution:
    def minOperations(self, l: List[str]) -> int:
        c=0
        for i in l:
            if i=="../":
                if c>0:
                    c-=1
            elif i=="./":
                continue
            else:
                c+=1
        if c<0:
            return 0
        return c