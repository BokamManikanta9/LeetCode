class Solution:
    def countSeniors(self, d: List[str]) -> int:
        c=0
        for i in d:
            x=(i[-4]+i[-3])
            if int(x)>60:
                c+=1
        return c