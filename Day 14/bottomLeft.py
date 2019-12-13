class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.bottom = None
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return self.bottom
        elif(root.left is not None):
            self.findBottomLeftValue(root.left)
            if(root.right is not None):
                self.findBottomLeftValue(root.right)
        elif(root.right is not None):
                self.findBottomLeftValue(root.right)
        elif(root.left is None and root.right is None):
            self.bottom = root.val
        
            
            
