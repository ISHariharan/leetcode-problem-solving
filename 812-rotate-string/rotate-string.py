class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if (len(s) != len(goal)):
            return False
        newString = s + s
        return goal in newString