class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        print(d)
        for m,n in d.items():
            if n==1:
                l.append(m)
        return l