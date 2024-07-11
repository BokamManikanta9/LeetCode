class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        x=""
        for i in s:
            if i=="(":
                l.append(x)
                x=""
                # continue
            elif i==")":
                y=l.pop()
                x=y+x[::-1]
            else:
                x+=i
        print(x)
        return x
