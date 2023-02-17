# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        min_diff = float('inf')
        print res
        for i in range(1, len(res)):
            min_diff = min(min_diff, res[i] - res[i - 1])
        return min_diff
