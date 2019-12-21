class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



def insertIntoBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """

    curr = root
    if(curr is None):
        return
    else:
        
        if(curr.val>val):
            if(curr.right is not None)
            self.insertIntoBST(curr.right, val)
        elif(curr.right is not None):
            self.insertIntoBST(curr.left, val)
            
        
