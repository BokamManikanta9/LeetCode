class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        nums.reverse()
        print(nums)
        if len(nums)<3:
            return nums[0]
        else:
            return nums[2]