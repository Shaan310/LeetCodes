class Solution(object):
    def smallestNumber(self, n, t):
        l = n
        while True:
            d = []
            temp = l
            if temp == 0:
                d.append(0)   
            while temp > 0:
                d.append(temp % 10)
                temp //= 10
            product = 1
            for dig in d:
                product *= dig
            if product % t == 0:
                return l
            l+= 1

        
        