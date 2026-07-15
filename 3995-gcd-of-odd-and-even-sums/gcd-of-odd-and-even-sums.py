class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOfEvenNumbers = n * (n+1)
        sumOfOddNumbers = n ** 2
        maxiGCD = 0
        for divisor in range(min(sumOfEvenNumbers, sumOfOddNumbers), -1, -1):
            if sumOfEvenNumbers % divisor == 0 and sumOfOddNumbers % divisor == 0:
                return divisor
        return maxiGCD