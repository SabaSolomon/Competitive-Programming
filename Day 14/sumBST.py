# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
    def recursiveSearch(self, root, L, R):
        if(root is None):
            return
        if(root.val >= L and root.val <= R):
            self.sum += root.val
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)
        elif(root.val <= L):
            self.rangeSumBST(root.right, L, R)
        elif(root.val >= R):
            self.rangeSumBST(root.left, L, R)
            
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.recursiveSearch(root, L, R);
        return self.sum
        
        

