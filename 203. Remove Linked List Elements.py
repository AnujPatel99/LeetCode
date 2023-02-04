# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        prev = 0
        while temp:
            if temp.val == val and temp == head:
                head = head.next
            elif temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head
