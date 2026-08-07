class Solution(object):
    def toLowerCase(self, s):
        r = ""
        for ch in s:
            if 'A' <= ch <= 'Z':
                r += chr(ord(ch) + 32)
            else:
                r += ch
        return r