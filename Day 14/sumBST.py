from tail_recursion import tail_recursive, recurse

@tail_recursive
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
    def tailRecursionSum(self, root, L, R, sum):
        if(root is None):
            return sum
        
        print("R",root.val)
        if(root.val >= L and root.val <= R):
            self.tailRecursionSum(root.left, L, R, sum = sum+root.val)
            return self.tailRecursionSum(root.right, L, R, sum = sum+root.val)
        elif(root.val <= L):
            return self.tailRecursionSum(root.right, L, R, sum = sum+root.val)
        elif(root.val >= R):
            return self.tailRecursionSum(root.left, L, R, sum = sum+root.val)
            
    def recursiveSearch(self, root, L, R):
        if(root is None):
            return 0
        
        if(root.val >= L and root.val <= R):
            sum = root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
            return sum
        elif(root.val <= L):
            return self.rangeSumBST(root.right, L, R)
        elif(root.val >= R):
            return self.rangeSumBST(root.left, L, R)
            
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        return self.recursiveSearch(root, L, R)
        
        
t = TreeNode(5)

t1 = TreeNode(1)
t.left = t1
t.right = TreeNode(6)
t1.right = TreeNode(23)
s = Solution()
print(s.rangeSumBST(t, 1, 6))
