from fractions import gcd
class Solution(object):
    def hasGroupsSizeX(self, deck):
        deck.sort()
        s={}
        for i in range(len(deck)):
            if deck[i] in s:
                s[deck[i]]+=1
            else:
                s[deck[i]]=1
        o=0
        for fr in s.values():
            o=gcd(o,fr)
        return o>1

        