class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l=[]
        for i in arr:
            if arr.count(i)==1:
                l.append(i)
        p=k-1
        if k<=len(l):
            return l[p]      
        else:
            return ""