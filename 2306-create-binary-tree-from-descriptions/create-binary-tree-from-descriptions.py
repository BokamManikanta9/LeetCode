# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, d: List[List[int]]) -> Optional[TreeNode]:
        ans={}
        s=set()
        for x,y,left in d:
            if x not in ans:
                ans[x]=TreeNode(x)
            if y not in ans:
                ans[y]=TreeNode(y)
            if left:
                ans[x].left=ans[y]
            else:
                ans[x].right=ans[y]
            s.add(y)
        for x,y,left in d:
            if x not in s:
                return ans[x]