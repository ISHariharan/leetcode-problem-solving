class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = {}
        paranthesis = []
        for index in range(len(s)):
            if s[index] == '(':
                stack[index] = ')'
            elif s[index] == ')':
                if len(stack) == 1:
                    i, c = stack.popitem()
                    paranthesis.append(i)
                    paranthesis.append(index)
                    
                else:
                    stack.popitem()
        newString = [s[index] for index in range(len(s)) if index not in paranthesis]
        return "".join(newString)
