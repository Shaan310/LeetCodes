class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        r = 2
        while True:
            c = num // r
            if c > r:
                r += 1
            else:
                if r * r == num:
                    return True
                if (r - 1) * (r - 1) == num:
                    return True
                return False
        