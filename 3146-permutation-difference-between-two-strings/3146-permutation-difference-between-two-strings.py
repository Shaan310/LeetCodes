class Solution(object):
    def findPermutationDifference(self, s, t):
        p={}
        q={}
        i=0
        j=0
        for so in s:
            p[so]=i
            i+=1
        for to in t:
            q[to]=j
            j+=1
        c=0
        for so in s:
            c+=(abs(p[so]-q[so]))
        return c



        