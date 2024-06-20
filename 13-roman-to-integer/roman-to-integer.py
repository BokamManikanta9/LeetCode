class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        i=0
        while i<len(s)-1:
            if s[i]=='I':
                if s[i+1]!='V' and s[i+1]!='X':
                    sum+=1
                    i+=1
                elif s[i+1]=='V':
                    sum+=4
                    i+=2
                elif s[i+1]=='X':
                    sum+=9
                    #continue
                    i+=2
            #print(sum,end=' ')
            elif s[i]=='V':
                sum+=5
                i+=1
            #print(sum,end=' ')
            elif s[i]=='X':
                if s[i+1]!='L' and s[i+1]!='C':
                    sum+=10
                    i+=1
                elif s[i+1]=='L':
                    sum+=40
                    #continue
                    i+=2
                elif s[i+1]=='C':
                    sum+=90
                    i+=2
                    #continue
            #print(sum,end=' ')
            elif s[i]=='L':
                sum+=50
                i+=1
            #print(sum,end=' ')
            elif s[i]=='C':
                if s[i+1]!='D' and s[i+1]!='M':
                    sum+=100
                    i+=1
                elif s[i+1]=='D':
                    sum+=400
                    i+=2
                    #continue
                elif s[i+1]=='M':
                    sum+=900
                    #continue
                    i+=2
            #print(sum,end=' ')
            elif s[i]=='D':
                sum+=500
                i+=1
            #print(sum,end=' ')
            elif s[i]=='M':
                sum+=1000
                i+=1
            #print(sum,end=' ')
        if s=="X":
            return 10
        if len(s)>1 and  s[-1]=='I':
            sum+=1
        if len(s)>1 and s[-1]=='X'and s[-2]!='I':
            sum+=10
        if len(s)>1 and s[-1]=='C' and s[-2]!='X':
            sum+=100
        if len(s)>1 and  s[-1]=='V' and s[-2]!='I':
            sum+=5
        if len(s)>1 and  s[-1]=='L' and s[-2]!='X':
            sum+=50
        if len(s)>1 and  s[-1]=='D' and s[-2]!='C':
            sum+=500
        if len(s)>1 and  s[-1]=='M' and s[-2]!='C':
            sum+=1000
        if len(s)==1 and s[0]=='I':
            sum+=1
        if len(s)==1 and s[0]=='V':
            sum+=5
        if len(s)==1 and s[0]=='x':
            sum+=10
        if len(s)==1 and s[0]=='L':
            sum+=50
        if len(s)==1 and s[0]=='C':
            sum+=100
        if len(s)==1 and s[0]=='D':
            sum+=500
        if len(s)==1 and s[0]=='M':
            sum+=1000
        
        return sum