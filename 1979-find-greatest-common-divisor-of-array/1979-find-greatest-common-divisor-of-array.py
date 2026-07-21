from fractions import gcd
class Solution(object):
    def findGCD(self, nums):
        arr= nums
        a=max(arr)
        b=min(arr)
        r= gcd(a,b)
        return r
        