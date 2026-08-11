class Solution(object):
    def romanToInt(self, s):
        ro={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        c=0
        t=0
        for st in s:
            if ro[st]>t:
                c+=ro[st]-(2*t)
            else:
                c+=ro[st]
            t=ro[st]
        return c
        