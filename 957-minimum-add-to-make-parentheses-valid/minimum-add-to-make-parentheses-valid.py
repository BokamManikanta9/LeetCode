class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c=0
        c1=0
        for i in s:
            if i=="(":
                c+=1
            elif i==")" and c>0:
                c-=1
            elif i==")":
                c1+=1
        print(c,c1)
        return c+c1