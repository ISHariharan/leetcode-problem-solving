class Solution:
    def romanToInt(self, s: str) -> int:
        roman_hash = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D": 500, "M" : 1000}
        multiply = 1
        result = 0
        temp = ""
        temp_value = 0
        for char in s:
            if temp == "":
                temp = char
                temp_value = roman_hash[char]
            elif temp == char:
                multiply += 1
            elif temp_value > roman_hash[char]:
                result += temp_value * multiply
                temp = char
                temp_value = roman_hash[char]
                multiply = 1
            elif temp_value < roman_hash[char]:
                result += roman_hash[char] - temp_value
                temp = ""
                temp_value = 0
        if temp_value > 0:
            result += temp_value * multiply
        return result