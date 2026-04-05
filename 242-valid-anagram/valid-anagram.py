class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s = sorted(s)
        t = sorted(t)
        for index in range(len(s)):
            if s[index] != t[index]:
                return False
        return True