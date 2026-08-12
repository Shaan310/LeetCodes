class Solution(object):
    def decodeMessage(self, key, message):
        a='a'
        s={}
        for k in key:
            if k==" ":
                    continue
            if k not in s:
                s[k]=a
                a=chr(ord(a) + 1)
        p=""
        for m in message:
            if m==" ":
                p+=(" ")
            else:
                p+=(s[m])
        return p


        