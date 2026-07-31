class Solution(object):
    def maxProfit(self, prices):
        s=prices[0]
        b=0
        for pr in prices:
            s=min(pr,s)
            b=max(b,pr-s)
        return b

            

            

        