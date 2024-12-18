class Solution:
    def finalPrices(self, p: List[int]) -> List[int]:
        l=[]

        for i in range(len(p)):
            f=0
            for j in range(i+1,len(p)):
                # print(p[j])
                if j>i and p[j]<=p[i]:
                    l.append(p[i]-p[j])
                    f=1
                    break
            if f==0:
                l.append(p[i])
        # l.append(p[-1])
        return l