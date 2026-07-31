class Solution(object):
    def lengthOfLastWord(self, s):
        p=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                p+=1
            if p>0 and s[i]==" ":
                return p
        return p

        