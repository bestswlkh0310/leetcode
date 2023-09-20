# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        now = head

        if now == None: return None
        
        while now.next != None:
            if now.val == now.next.val: 
                now.next = now.next.next
            else:
                now = now.next # not none
            
        return head
    