'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i,x in enumerate(nums):
            if x in dict:
                dict[x].append(i)
            else:
                dict[x]=[i]
        
        for x in dict.keys():
            indices = dict[x]
            if len(indices)>1:
                last = indices[0]
                for y in xrange(1,len(indices)):
                    if abs(indices[y]-last)<=k:
                        return True
                    last = indices[y]
        return False            