class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        c=0
        nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]<=nums[i-1]:
        #         a=nums[i-1]+1
        #         c+=a-nums[i]
        #         nums[i]=a
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i+1]=nums[i+1]+1
                c+=1
            if nums[i]>nums[i+1]:
                x=nums[i]+1
                c+=x-nums[i+1]
                nums[i+1]=x
        return c