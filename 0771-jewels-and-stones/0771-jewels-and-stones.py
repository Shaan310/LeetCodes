class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        jewel = set(jewels)
        for s in stones:
            if s in jewel:
                c+=1
        return c        