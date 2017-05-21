'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        k = sorted(nums)
        if k==nums:
            return 0
        
        begin = 0
        for i in xrange(0,len(k)):
            if(nums[i]!=k[i]):
                begin = i
                break
        end = len(k)-1
        for i in xrange(len(k)-1, 0, -1):
            if nums[i]!=k[i] :
                end = i
                break
        
        return end-begin+1