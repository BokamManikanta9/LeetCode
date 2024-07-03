class Solution {
public:
    int minDifference(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int ans=nums[n-1]-nums[0];
        if(n<=4){
            return 0;
        }
        for(int i=0;i<4;i++){
            ans=min(ans,nums[n-1-i]-nums[3-i]);
        }
        return ans;

    }
};