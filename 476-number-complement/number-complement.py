class Solution:
    def findComplement(self, num: int) -> int:
        s=""
        while num!=0:
            if num&1:
                s+='0'
            else:
                s+='1'
            num=num>>1
        print(s)
        return int(s[::-1],2)