'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
'''


def intersection(nums1, nums2):
    if len(nums1)>0 and len(nums2)>0:
        res = set(nums1).intersection(nums2)
        return list(res)
    else:
        return []


print intersection([],[])
