class Solution(object):
    def reverseString(self, s):
        n=len(s)
        j=n-1
        for i in range(n//2):
            s[i],s[j]=s[j],s[i]
            j-=1
        
        