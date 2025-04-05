# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], tar: int) -> bool:
        if not root:
            return False
    
        tar=tar-root.val
        if (not root.right) and (not root.left) and tar==0:
            return True

        return self.hasPathSum(root.left,tar) or self.hasPathSum(root.right,tar)
