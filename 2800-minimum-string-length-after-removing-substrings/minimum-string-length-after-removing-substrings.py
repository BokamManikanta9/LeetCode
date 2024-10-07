class Solution:
    def minLength(self, s: str) -> int:
        l=[]
        for i in s:
            if i=="B" and len(l)!=0 and l[-1]=="A":
                l.pop()
            elif i=="D" and len(l)!=0 and l[-1]=="C":
                l.pop()
            else:
                l.append(i)
        print(l)
        return len(l)