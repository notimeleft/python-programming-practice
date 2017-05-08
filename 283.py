#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].



def moveZeroes(nums):
    zeros = 0
    i = 0
    while(0 in nums):
        if len(nums)==0:
            break
        if nums[i]==0:
            del(nums[i])
            zeros+=1
            continue
        i+=1
    nums+=[0]*zeros


moveZeroes([0,1,0,3,12])
