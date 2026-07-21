class Solution(object):
    def canReach(self, start, target):
        c1 = (start[0]+start[1])%2
        c2 = (target[0]+target[1])%2
        return c1 == c2
        