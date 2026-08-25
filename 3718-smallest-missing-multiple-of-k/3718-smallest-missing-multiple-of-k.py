class Solution(object):
    def missingMultiple(self, nums, k):
        c=1
        while True:
            if k*c not in nums:
                return k*c
            c+=1
        