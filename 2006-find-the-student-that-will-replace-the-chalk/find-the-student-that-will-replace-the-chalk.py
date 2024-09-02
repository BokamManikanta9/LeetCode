class Solution:
    def chalkReplacer(self, c: List[int], k: int) -> int:
        n=len(c)
        s=sum(c)
        print(n,k,s)
        x=k%s
        for i in range(len(c)):
            if x<c[i]:
                return i
            x-=c[i]
            
        # i=0
        # l=len(c)
        # while True:
        #     k-=c[i]
        #     i+=1
        #     if i==l:
        #         i=0
        #     if c[i]==k:
        #         return 0
        #     if c[i]>k:
        #         return i