class Solution(object):
    def duplicateNumbersXOR(self, nums):
        c=0
        s={}
        for num in nums:
            if num not in s:
                s[num]=1
            else:
                c^=num
        return c
        
        