class Solution {
public:
    int minOperations(vector<string>& l) {
        int c=0;
        for(int i=0;i<l.size();i++){
            if(l[i]=="../"){
                if(c>0){
                    c-=1;
                }
            }
            else if(l[i]=="./"){
                continue;
            }
            else{
                c+=1;
            }
        }
        if(c<0){
            return 0;
        }
        else{
            return c;
        }
    }
};