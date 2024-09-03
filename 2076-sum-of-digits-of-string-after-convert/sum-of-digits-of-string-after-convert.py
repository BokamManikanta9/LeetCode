class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums= {chr(i): i - 96 for i in range(97, 123)}
        s1=""
        for i in s:
            s1+=str(nums[i])
        print(s1)
        # s1=int(s1)
        s2=0
        for i in range(k):
            l= [int(x) for x in s1]
            print(l)
            s2=sum(l)
            s1=str(s2)
        print(s2)
        return s2
