class Solution(object):
    def minOperations(self, nums, k):
        s=sum(nums)
        i=0
        while True:
            if (sum(nums)-i)%k==0:
                return i
            i+=1
        