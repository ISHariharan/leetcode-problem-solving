class Solution:
    # d÷ef getSequentialDigits(self, substr : List[int], low : int, high : int) -> List[int]:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        number = "123456789"
        substr = []
        length = len(number)
        for i in range(length):
            for j in range(i + 1, length + 1):
                num = int(number[i : j])
                if num >= low and num <= high:
                    substr.append(num)
        return sorted(substr)