class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         if len(arr[i:j+1])==3:
        #             c=0
        #             for i in arr[i:j+1]:
        #                 if i%2!=0:
        #                     c+=1
        #             if c==3:
        #                 return True
        # return False
        c=0
        for i in arr:
            if i%2!=0:
                c+=1
            else:
                c=0
            if c==3:
                return True
        return False