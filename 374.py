'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0)
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = (start+end)/2
        
        while(guess(mid)!=0):
            mid = (start+end)/2
            #this line is the most tricky part! We must add 1 to the mid point here to avoid an infinite loop. 
            if guess(mid)==1:
                start = mid+1
            
            if guess(mid)==-1:
                end = mid
        
        return mid 