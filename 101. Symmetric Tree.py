# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and isMirror(l.left, r.right) and isMirror(l.right, r.left)

        return isMirror(root.left, root.right)
