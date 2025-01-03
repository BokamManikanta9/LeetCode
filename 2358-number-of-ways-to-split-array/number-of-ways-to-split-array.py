class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ts=sum(nums)
        s=0
        c=0
        for i in range(len(nums)-1):
            s+=nums[i]
            if s>=ts-s:
                c+=1
        return c



        # i=0
        # c=0
        # n=len(nums)
        # while i!=len(nums)-1:
        #     if sum(nums[0:i+1])>=sum(nums[i+1:]):
        #         c+=1
        #     i+=1
        # return c
     