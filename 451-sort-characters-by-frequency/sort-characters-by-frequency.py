from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        reverseSorted = dict(sorted(count.items(), key=lambda item:-item[1]))
        return ''.join(char * count[char] for char in reverseSorted)