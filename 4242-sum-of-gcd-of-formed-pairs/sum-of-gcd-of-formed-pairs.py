class Solution:
    def gcd(x : int, y : int) -> int:
        if y == 0:
            return x
        return gcd(y, x % y)
    def gcdSum(self, nums: list[int]) -> int:
        mx = -1
        prefixGcd = []
        for num in nums:
            mx = max(num, mx)
            prefixGcd.append(gcd(num, mx))
        low = 0
        high = len(prefixGcd) - 1
        summation = 0
        prefixGcd = sorted(prefixGcd)
        while low < high:
            summation += gcd(prefixGcd[low], prefixGcd[high])
            low += 1
            high -= 1
        return summation


        