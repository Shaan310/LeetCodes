class Solution(object):
    def minMoves(self, nums):
        c=max(nums)
        r=0
        for nu in nums:
            r+=(c-nu)
        return r