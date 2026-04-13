class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[len(strs) - 1]
        pointer = 0
        while pointer < len(first) and pointer < len(last):
            if first[pointer] != last[pointer]:
                if pointer == 0:
                    return ""
                return first[:pointer]
            pointer += 1
        return first[:pointer]
            
