class Solution:
    def largestOddNumber(self, s: str) -> str:
        pointer = 0
        largest = ""
        while pointer < len(s):
            if int(s[pointer]) % 2 == 1:
                largest = s[:pointer + 1]
            pointer += 1
        if largest == 0:
            return ""
        return largest