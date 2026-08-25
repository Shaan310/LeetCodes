class Solution(object):
    def missingMultiple(self, nums, k):
        l=set(nums)
        c=1
        while True:
            if k*c not in l:
                return k*c
            c+=1
        