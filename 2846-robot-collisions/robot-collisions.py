class Solution:
    def survivedRobotsHealths(self, p: List[int], h: List[int], d: str) -> List[int]:
        n=len(p)
        r=list(range(n))
        l=[]
        r.sort(key=lambda x: p[x])
        for i in r:
            if d[i]=='R':
                l.append(i)
            else:
                while l and h[i]>0:
                    top=l.pop()
                    if h[top]>h[i]:
                        h[top]-=1
                        h[i]=0
                        l.append(top)
                    elif h[top]<h[i]:
                        h[i]-=1
                        h[top]=0
                    else:
                        h[i]=0
                        h[top]=0
        print(l)
        print(h)
        return [i for i in h if i>0]