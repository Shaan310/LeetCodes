class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        c=0
        for nu in nums:
            for n in str(nu):
                if n==str(digit):
                    c+=1
        return c
        