class Solution(object):
    def findPermutationDifference(self, s, t):
        p={}
        q={}
        i=0
        j=0
        for i in range(len(s)):
            p[s[i]]=i
            q[t[i]]=i
        c=0
        for so in s:
            c+=(abs(p[so]-q[so]))
        return c



        