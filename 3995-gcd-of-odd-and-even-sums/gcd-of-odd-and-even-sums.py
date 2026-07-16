class Solution:
    def gcd(x, y) -> int:
        if y == 0:
            return x
        return gcd(y, x%y)
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOfEvenNumbers = n * (n+1)
        sumOfOddNumbers = n ** 2
        return gcd(sumOfEvenNumbers, sumOfOddNumbers)