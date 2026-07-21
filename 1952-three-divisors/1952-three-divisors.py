class Solution(object):
    def isThree(self, n):
        c=0
        for i in range (2,n):
            if n%i==0:
                c+=1
        if c==1:
            return True
        return False


        