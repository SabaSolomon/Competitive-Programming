class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def reverseKGroup(head, k):
    count = 1
    curr = head
    prev = curr
    nextNode = curr.next
    while(curr is not None):
        if(k==1):
            break
        if(count == k):
            nextNode
        else:
            count += 1
            
        
        
        
