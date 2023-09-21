# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.t = False
        def search(r, i):
            if r.left == None and r.right == None and i == targetSum:
                self.t = True
            if r.left != None:
                search(r.left, i + r.left.val)
            if r.right != None:
                search(r.right, i + r.right.val)
        if root == None:
            return False
        search(root, root.val)
        
        return self.t
    