# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = { head: "" }
        
        while head != None:
            if head.next in lst:
                return head.next
            else:
                lst[head] = ""
            head = head.next
        