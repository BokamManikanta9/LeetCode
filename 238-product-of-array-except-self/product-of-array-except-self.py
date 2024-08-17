class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[1]*n
        left=1
        rigth=1 
        for i in range(n):
            l[i]=left
            left*=nums[i] 
        for i in range(n-1,-1,-1):
            l[i]*=rigth
            rigth*=nums[i]
        return l