class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for index in range(len(s)):
            newString = s[index:] + s[:index]
            if (newString == goal):
                return True
        return False