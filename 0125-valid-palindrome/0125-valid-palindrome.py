class Solution(object):
    def isPalindrome(self, s):
        m=""
        for ch in s:
            if ch.isalnum():
                m+=ch.lower()
        return m==m[::-1]
        