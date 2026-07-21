class Solution(object):
    def convertTemperature(self, celsius):
        c = celsius
        fahrenheit = (c * 1.80)+ 32.00
        kelvin = c + 273.15
        ans = [kelvin, fahrenheit]
        return ans
        
        
        