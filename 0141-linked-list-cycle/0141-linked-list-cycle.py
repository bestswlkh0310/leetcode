# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = []
        
        if head == None: return False
        
        while head.next != None:
            if head.next in lst:
                return True
            else:
                lst.append(head.next)
            head = head.next
            
        return False