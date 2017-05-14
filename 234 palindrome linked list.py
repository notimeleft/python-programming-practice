'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

Subscribe to see which companies asked this question.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        #get length of linked list, find midpoint
        length = 0
        current = head
        while(current):
            length+=1
            current=current.next
        mid = length/2
        
        #edge cases: 2? check if 1st==2nd element. 1 or 0? always true. 
        if(length<3):
            if length==2:
                return head.val==head.next.val
            return True
            
        #traverse to the midpoint node
        current = head
        while(mid!=0):
            current = current.next
            mid-=1
        
        #reverse the second half of the list
        end = self.reverse(current)
        start = head
        
        #traverse from both ends of the list, checking whether each end is equal. Return false if not. 
        while(start and end):
            if start.val!=end.val:
                return False
            start = start.next
            end = end.next
        return True
        
    def reverse(self,head):
        prev = head
        current = head.next
        nxt = current.next
        prev.next=None
        while(nxt):
            current.next=prev
            prev = current
            current = nxt
            nxt = nxt.next
        current.next=prev
        return current    