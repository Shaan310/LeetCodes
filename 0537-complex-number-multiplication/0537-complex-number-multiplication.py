class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        a1,a2=num1[:-1].split('+')
        b1,b2=num2[:-1].split('+')
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)
        a=(a1*b1)-(a2*b2)
        b=(a1*b2)+(b1*a2)
        return str(a)+"+"+str(b)+"i"


        