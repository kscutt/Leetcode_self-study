# Recursive solution 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      
        if root is None: return root  # nothing to invert 
        
        # traverse and swap 
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        # creates a tuple that is swapped 
        
        return root
