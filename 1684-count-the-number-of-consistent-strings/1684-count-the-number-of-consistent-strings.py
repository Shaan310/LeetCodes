class Solution(object):
    def countConsistentStrings(self, allowed, words):
        a=set(allowed)
        r=0
        for word in words:
            p=1
            for c in word:
                if c not in a:
                    p=0
                    break
            r+=p
        return r

        