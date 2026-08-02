class Solution(object):
    def stoneGame(self, piles):
        one=0
        two=0
        while piles:
            m=0
            m = max(piles[0],piles[-1])
            one+=m
            piles.remove(m)
            if piles:
                o=0
                o += min(piles[0],piles[-1])
                two+=o
                piles.remove(o)
        return one>=two
        