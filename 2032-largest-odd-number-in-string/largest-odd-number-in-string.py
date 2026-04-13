class Solution:
    def largestOddNumber(self, s: str) -> str:
        pointer = len(s) - 1
        largest = ""
        while pointer >= 0:
            if int(s[pointer]) % 2 == 1:
                return s[:pointer + 1]
            pointer -= 1
        return ""