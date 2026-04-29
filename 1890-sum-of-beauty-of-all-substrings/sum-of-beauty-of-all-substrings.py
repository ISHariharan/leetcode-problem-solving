class Solution:
    def calculateBeauty(self, substring: str) -> int:
        maximum = 0
        minimum = len(substring)
        for char in set(substring):
            count = substring.count(char)
            if count > maximum:
                maximum = count
            if count < minimum:
                minimum = count
        return maximum - minimum
    def beautySum(self, s: str) -> int:
        beauty = 0 
        substrings = []
        length = len(s)
        for left in range(length):
            for right in range(length):
                substrings.append(s[left:right + 1])
        for substring in substrings:
            beauty += self.calculateBeauty(substring)
        return beauty