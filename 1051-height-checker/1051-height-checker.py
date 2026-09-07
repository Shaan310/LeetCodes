class Solution(object):
    def heightChecker(self, heights):
        c=0
        exp=heights[:]
        exp.sort()
        for i in range(len(heights)):
            if exp[i]!=heights[i]:
                c+=1
        return c
        