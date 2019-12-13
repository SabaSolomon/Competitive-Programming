class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(head):
    result = None
    while head:
        current = head
        head = head.next
        if not result or current.val < result.val:
            current.next = result;
            result = current;
        else:
            find = result;
            while find and find.next is not None and current.val > find.next.val:
                find = find.next
            current.next = find.next
            find.next = current
    return result

        
list = ListNode(2)
list1 = ListNode(1)
list.next = list1


list3 = ListNode(3)
list1.next = list3
list4 = ListNode(2)
list3.next = list4
##list5 = ListNode(2)
##list4.next = list5
list = insertionSortList(list)

curr = list
while(curr is not None):
    print(curr.val)
    curr = curr.next

##list2 = ListNode(4)
##l1 = ListNode(-1)
##list2.next = l1
##listr = insertionSortList(list2)
##print("\n############")
##
##
##print("\n############")
##cu = listr
##while(cu is not None):
##    print(cu.val)
##    cu = cu.next
##
##list2 = ListNode(4)                   
##                    
##                    
##print("\n############")
##cu = listr
##while(cu is not None):
##    print(cu.val)
##    cu = cu.next
