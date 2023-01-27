# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        copy = head
        while head:
            stack.append(head.val)
            head = head.next
        median = math.ceil(len(stack) / 2.0)
        if len(stack) % 2 == 0: #Checking if their are two middle nodes, getting the second one
            median += 1
        head = copy
        for x in range(int(median) - 1):
            head = head.next
        return head
