#5(11..,221,212,122,+4)=8
class Solution(object):
    def climbStairs(self, n):
        c=[1,2]
        if n<3:
            return n
        for i in range (n-2):
            r=c[0]+c[1]
            c[0]=c[1]
            c[1]=r
        return r
        