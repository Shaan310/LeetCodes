class Solution(object):
    def maximum69Number (self, num):
        r=list(str(num))
        for i in range(len(r)):
            if r[i] == "6":
                r[i] = "9"
                break
        s="".join(r)
        return int(s)



        
        