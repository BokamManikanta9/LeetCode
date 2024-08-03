class Solution:
    def canBeEqual(self, t: List[int], arr: List[int]) -> bool:
        t.sort()
        arr.sort()
        if t==arr:
            return True
        else:
            return False