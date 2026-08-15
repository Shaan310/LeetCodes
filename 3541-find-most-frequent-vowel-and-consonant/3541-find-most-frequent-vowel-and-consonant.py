class Solution(object):
    def maxFreqSum(self, s):
        p={'a':0,'e':0,'i':0,'o':0,'u':0}
        c={'empty':0}
        for sus in s:
            if sus in p:
                p[sus]+=1
            else:
                if sus in c:
                    c[sus]+=1
                else:
                    c[sus]=1
        return max(p.values()) + max(c.values())
        