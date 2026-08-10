class Solution(object):
    def addDigits(self, num):
        while True:
            if num<10:
                return num
            else:
                r=0
                while num>0:
                    r+=(num%10)
                    num=num//10
            num=r
        