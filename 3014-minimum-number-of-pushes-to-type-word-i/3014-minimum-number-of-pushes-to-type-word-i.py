class Solution(object):
    def minimumPushes(self, word):
        s={}
        c=0
        for wr in word:
            if wr in s:
                s[wr]+=1
            else:
                s[wr]=1
        freq=sorted(s.values(),reverse=True)
        for i in range(len(freq)):
            c +=(i//8 +1)*freq[i]
        return c
        