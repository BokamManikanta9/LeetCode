class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        c=0
        f=1
        l=[]
        if x>=y:
            p=x
            q=y
        else:
            p=y
            q=x
        if x>=y:
            for i in s:
                l.append(i)
                if len(l)>=2:
                    if l[-2]=='a' and l[-1]=='b':
                        l.pop()
                        l.pop()
                        c+=p
                        print(c,end=" ")
            a=""
            l1=[]
            for i in l:
                a+=i
            print(a)
            for i in a:
                l1.append(i)
                if len(l1)>=2:
                    if l1[-2]=='b' and l1[-1]=='a':
                        l1.pop()
                        l1.pop()
                        c+=q

            print(l)
            print(l1)
            print(c)
            return c
        else:
            for i in s:
                l.append(i)
                if len(l)>=2:
                    if l[-2]=='b' and l[-1]=='a':
                        l.pop()
                        l.pop()
                        c+=y
                        print(c,end=" ")
            a=""
            l1=[]
            for i in l:
                a+=i
            print(a)
            for i in a:
                l1.append(i)
                if len(l1)>=2:
                    if l1[-2]=='a' and l1[-1]=='b':
                        l1.pop()
                        l1.pop()
                        c+=x

            print(l)
            print(l1)
            print(c)
            return c
            