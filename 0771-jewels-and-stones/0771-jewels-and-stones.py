class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for s in stones:
            if s in set(jewels):
                c+=1
        return c        