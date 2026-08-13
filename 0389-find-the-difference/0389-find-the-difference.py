class Solution(object):
    def findTheDifference(self, s, t):
        c=0
        for i in range(len(s)):
            c^=(ord(s[i])^ord(t[i]))
        c=c^ord(t[-1])
        return chr(c)