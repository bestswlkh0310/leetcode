# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = 0

        idx = 0
        obj = l1

        while obj.next != None:
            result += obj.val * (10 ** idx)
            obj = obj.next
            idx += 1
        result += obj.val * (10 ** idx)

        idx = 0
        obj = l2

        while obj.next != None:
            result += obj.val * (10 ** idx)
            obj = obj.next
            idx += 1
        result += obj.val * (10 ** idx)
        
        ret = []
        lst = list(map(int, list(str(result))))
        nextNode = None
        for i in lst:
            node = ListNode(val=i)
            if nextNode != None:
                node.next = nextNode
            nextNode = node

        return nextNode
        
        