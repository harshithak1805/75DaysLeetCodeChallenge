class Solution:
    def isValidBST(self, root):
        return self.helper(root,float("-inf"),float("inf"))
    def helper(self,root,minval,maxval):
        if root is None:
            return True
        if (root.val<=minval) or (root.val >= maxval):
            return False
        return self.helper(root.left,minval,root.val) and self.helper(root.right,root.val,maxval)