class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                c+=1
        if nums[-1]>nums[0]:
            c+=1
        return c<=1













        # l=[]
        # l1=[]
        # for i in range(len(nums)-1):
        #     if nums[i+1]>=nums[i]:
        #         l.append(nums[i])
        #     # elif nums[i+1]<nums[i]:
        #     #     l.append(nums[i])
        #     else:
        #         l.append(nums[i])
        #         break
        # l.extend(nums[len(l):])
       
        # if len(l)>1 and l[-2]>nums[-1]:
        #     l.pop()
        # for i in nums:
        #     if i not in l:
        #         l1.append(i)
        # print(l,l1)
        # return l==sorted(nums)
        # if l==sorted(l) and l1==sorted(l1):
        #     return True
        # return False

        # c=0
        # for i in range(len(nums)-1):
        #     if nums[i+1]>nums[i] or nums[i+1]==nums[i]:
        #         continue
        #     elif nums[i]>nums[i+1] and c!=0:
        #         c-=1
        #     else:
        #         c+=1
        # print(c)
        # if c>1 or c<0:
        #     return False
        # elif nums[0]+1!=nums[-1] or nums[0]!=nums[-1]+1 and c==1:
        #     return True
        
        # return True
            
            