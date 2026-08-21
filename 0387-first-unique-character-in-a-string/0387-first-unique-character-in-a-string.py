class Solution(object):
    def firstUniqChar(self, s):
        c={}
        for st in s:
            if st not in c:
                c[st]=1
            else:
                c[st]+=1
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1
        