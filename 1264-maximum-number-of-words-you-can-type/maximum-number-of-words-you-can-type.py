class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        l=list(text.split(" "))
        c=0
        for i in l:
            for j in b:
                if j in i:
                    c+=1
                    break
        return len(l)-c