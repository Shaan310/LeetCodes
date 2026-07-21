class Solution(object):
    def isPalindrome(self, x):
        n = str(x)
        m = n[::-1]
        if m == n:
            return True
        return False

        