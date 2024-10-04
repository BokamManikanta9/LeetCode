class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        i=0
        j=len(s)-1
        s.sort()
        l=[]
        s1=[]
        while i<j:
            l.append(s[i]*s[j])
            s1.append(s[i]+s[j])
            i+=1
            j-=1
        print(l)
        print(s1)
        if len(set(s1))==1:
            return sum(l)
        else:
            return -1
