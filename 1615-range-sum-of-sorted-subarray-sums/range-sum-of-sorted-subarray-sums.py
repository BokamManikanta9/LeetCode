def SubArrays(arr, start, end,l):
    if end == len(arr):
        return
    elif start > end:
        return SubArrays(arr, 0, end + 1,l)
    else:
#         print(arr[start:end+1])
        l.append(sum(arr[start:end+1]))
        return SubArrays(arr, start + 1, end,l)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        SubArrays(nums,0,0,l)
        l.sort()
        print(l[left:right])
        return sum(l[left-1:right])%(10**9 + 7)