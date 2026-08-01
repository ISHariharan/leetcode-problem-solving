class Solution:
    def minimumPushes(self, word: str) -> int:
        unique_char = set(word)
        freqs = {}
        for char in unique_char:
            freqs[char] = word.count(char)
        freqs = dict(sorted(freqs.items(), key=lambda item:item[1], reverse=True))
        clicks = 0
        count = 0
        for freq in freqs.values():
            clicks = clicks + freq * (1 + (count // 8))
            count += 1
        return clicks
