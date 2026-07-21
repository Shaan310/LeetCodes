class Solution(object):
    def intToRoman(self, num):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanNum = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = ""

        for i in range(len(numbers)):
            while num >= numbers[i]:
                roman += romanNum[i]
                num -= numbers[i]

        return roman