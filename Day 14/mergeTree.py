class Solution(object):
    def recursiveMerge(self, t1, t2):
        if(t2 is None and t1 is None):
            return None
        else:
            if(t1 is None):
                t3 = TreeNode(t2.val)
                t3.left = self.recursiveMerge(None, t2.left)
                t3.right = self.recursiveMerge(None, t2.right)
            elif(t2 is None):
                t3 = TreeNode(t1.val)
                t3.left= self.recursiveMerge(t1.left, None)
                t3.right= self.recursiveMerge(t1.right, None)
            else:
                t3 = TreeNode(t1.val + t2.val)
                t3.left = self.recursiveMerge( t1.left, t2.left)
                t3.right = self.recursiveMerge(t1.right, t2.right)
            return t3
        
            
            
            
            
    def mergeTrees(self,  t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
       
        return self.recursiveMerge(t1, t2)
        


     

                    
