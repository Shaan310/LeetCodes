class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        s = set(nums)
        c=0
        for x in nums:
            if x + diff in s and x + 2*diff in s:
                c += 1
        return c




        