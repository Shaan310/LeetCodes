class Solution(object):
    def smallestNumber(self, n, t):
        l = n
        while True:
            digits = []
            temp = l
            if temp == 0:
                digits.append(0)   
            while temp > 0:
                digits.append(temp % 10)
                temp //= 10
            product = 1
            for digit in digits:
                product *= digit
            if product % t == 0:
                return l
            l+= 1

        
        