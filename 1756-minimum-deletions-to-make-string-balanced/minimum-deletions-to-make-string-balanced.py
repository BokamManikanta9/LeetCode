class Solution:
    def minimumDeletions(self, s: str) -> int:
        # s=list(s)
        # i=0
        # c=0
        # while i<len(s)-1:
        #     if s[i]=='b' and s[i + 1]=='a':
        #         s.pop(i)
        #         s.pop(i)
        #         c+=1
        #         if i>0:
        #             i-=1
        #     else:
        #         i+=1
        # return c
        d=0
        b=0
        for i in s:
            if i=='a':
                if b>0:
                    d+=1
                    b-=1
            elif i=='b':
                b+=1
        return d