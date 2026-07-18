class Solution:
    def gcd(self, x, y) -> int:
        if y == 0:
            return x
        return gcd(y, x % y)
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        smallest = nums[0]
        largest = nums[len(nums) - 1]
        GCD = self.gcd(smallest, largest)
        return GCD