class Solution:
    def minimumSteps(self, s: str) -> int:
        c=0
        tc=0
        for i in s:
            if i=="0":
                tc+=c
            else:
                c+=1
        return tc