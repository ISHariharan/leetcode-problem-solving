class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        if length <= 8:
            return length
        clicks = 0
        count = 1
        while length >= 0:
            if length - 8 < 0:
                clicks = clicks + count*(length)
                length -= 8
            elif length - 8 >= 0:
                clicks = clicks + count*8
                length -= 8
            
            count += 1
        return clicks
        