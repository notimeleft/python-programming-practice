# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
:type head: ListNode
:rtype: ListNode
"""
class Solution(object):
    def reverseList(self, head):

        if head==None:
            return None
        elif head.next == None:
            return head
        elif head.next.next == None:
            current = head.next
            current.next = head
            head.next = None
            return current
        else:
            current1 = head
            current2 = head.next
            current3 = head.next.next
            while(current1!=None):
                print current1.val
                current1 = current1.next
            return head
