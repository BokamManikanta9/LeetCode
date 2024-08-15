class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        c=0
        f=0
        t=0
        for i in b:
            if i==5:
                f+=1
            if i==10:
                t+=1
                if f>0:
                    f-=1
                else:
                    return False
            if i==20:
                if f>0 and t>0:
                    f-=1
                    t-=1
                elif f>2 and t<=0:
                    f-=3
                else:
                    return False
        return True

            