# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pre(root,x):
            if root:
                
                pre(root.left,x)
                pre(root.right,x)
                x.append(root.val)
        x=[]
        pre(root,x)
        return x