class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        print(nums)
        nums.sort()
        n=len(nums)
        x=len(nums)//2
        print(x)
        if n&1:
            return float(nums[x])
        else:
            
            return (float(nums[x-1])+float(nums[x]))/2.0
       
            
