class Solution:
    def findIfIsomorphic(self, s:str, t:str) -> bool:
        p1 = 0
        p2 = 0
        Mapper = {}
        length = len(s)
        while (p1 < length and p2 < length):
            exists = Mapper.get(s[p1])
            if (exists):
                if(t[p2] != exists):
                    return False
            else:
                # if s[p1] != t[p2]:
                Mapper[s[p1]] = t[p2]
            p1 += 1
            p2 += 1
        return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        with_s = self.findIfIsomorphic(s, t)
        with_t = self.findIfIsomorphic(t, s)
        return with_s and with_t