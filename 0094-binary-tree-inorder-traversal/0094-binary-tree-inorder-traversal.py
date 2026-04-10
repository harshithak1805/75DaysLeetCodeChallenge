# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def in_(root,x):
            if root:
                in_(root.left,x)
                x.append(root.val)
                in_(root.right,x)
        x=[]
        in_(root,x)
        return x    
