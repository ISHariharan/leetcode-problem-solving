class Solution:
    def isValid(self, s: str) -> bool:
        mirror_image = {"{" : "}", "(" : ")", "[": "]"}
        parantheses = []
        for char in s:
            if (char in parantheses) and (char == parantheses[len(parantheses) - 1]):
                parantheses.pop()
            else:
                parantheses.append(mirror_image.get(char))
        if len(parantheses) > 0:
            return False
        return True
        