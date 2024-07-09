class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        l=[]
        f=1
        for i in range(len(c)):
            if(f==1):
                t=sum(c[i])

                # l.append("a")
                l.append(t-c[i][0])
                f=0
            else:
                # l.append(t)
                if t>=c[i][0]:
                    t=t+c[i][1]
                    l.append(t-c[i][0])
                if t<c[i][0]:
                    t=sum(c[i])
                    l.append(t-c[i][0])
        print(l)
        print(sum(l)/len(l))
        return sum(l)/len(l)
            

            