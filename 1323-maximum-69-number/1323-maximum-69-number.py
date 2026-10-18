class Solution(object):
    def maximum69Number (self, num):
        r=list(str(num))
        for i in range(len(r)):
            if r[i] == "6":
                r[i] = "9"
                break
        return int(''.join(r))



        
        