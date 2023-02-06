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
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        stack1.reverse()
        stack2.reverse()
        num1 = num2 = ''
        for x in stack1:
            num1 += str(x)
        for x in stack2:
            num2 += str(x)
        val = int(num1) + int(num2)
        newList =[int(x) for x in str(val)][::-1]

        cur = dummy = ListNode(0)
        for e in newList:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
