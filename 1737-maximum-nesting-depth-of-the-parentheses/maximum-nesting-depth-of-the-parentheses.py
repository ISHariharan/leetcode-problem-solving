class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == ")":
                length = len(stack)
                if length > maxDepth:
                    maxDepth = length
                stack.pop()
        if len(stack) > maxDepth:
            maxDepth = len(stack)
        return maxDepth