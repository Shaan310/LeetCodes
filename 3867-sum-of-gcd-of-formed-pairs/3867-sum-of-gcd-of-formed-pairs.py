from fractions import gcd

class Solution(object):
    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = [0] * n
        mx = 0
        for i in range(n):
            x = nums[i]
            mx = max(mx, x)
            prefixGcd[i] = gcd(x, mx)
        prefixGcd.sort()
        r = 0
        for i in range(n // 2):
            r += gcd(prefixGcd[i], prefixGcd[n - 1 - i])    
        return r
        