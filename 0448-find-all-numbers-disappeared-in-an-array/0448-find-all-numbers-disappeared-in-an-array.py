class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        a=1
        s=set(nums)
        c=[]
        for i in range(n):
            if a+i not in s:
                c.append(a+i)
        return c

        