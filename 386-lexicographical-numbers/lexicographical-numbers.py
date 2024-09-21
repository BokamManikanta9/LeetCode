class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=[]
        for i in range(1,n+1):
            l.append(str(i))
        print(l)
        x=sorted(l)
        print(x)
        l=[int(i) for i in x]
        return l