class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def nextLargerNodes(head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
    stack = []
    ans = []
    count = 0
    while head:
        ans.append(0)
        while stack and stack[-1][0] < head.val:
            value, index = stack.pop()
            ans[index] = head.val
        stack.append((head.val, count))
        count += 1
        head = head.next
    return ans



    
list = ListNode(9)
list1 = ListNode(7)
list.next = list1

list2 = ListNode(6)
list1.next = list2
list3 = ListNode(7)
list2.next = list3
list4 = ListNode(6)
list3.next = list4
list5 = ListNode(9)
list4.next = list5

##list = ListNode(3)
##list1 = ListNode(3)
##list.next = list1
print(nextLargerNodes(list))
