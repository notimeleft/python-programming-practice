'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

:type candidates: List[int]
:type target: int
:rtype: List[List[int]]
'''
class Solution(object):

    def __init__(self):
        self.solutions = []
    def combinationSum(self, candidates, target):

        for i in candidates:
            print target, "-", i
            target = target - i
            print "=", target, "\n"

            if target == 0:
                return self.solutions.append(i)

            elif target>0:
                self.combinationSum(candidates,target)
            else:
                break
    def solve(self):
        return self.solutions


k = Solution()
k.combinationSum([2,3,7],7)
print k.solve()
