'''
Given a linked list, determine if it has a cycle in it.
'''

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
        seen = set()
        current = head
        while(current):
            if current not in seen:
                seen.add(current)
            else:
                return True
            current = current.next
        return False  