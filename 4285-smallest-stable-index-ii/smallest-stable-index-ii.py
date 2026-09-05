class Solution:
    def findMaximum(self, nums) -> list[int]:
        maximum = float('-inf')
        result = []
        for num in nums:
            if maximum < num:
                maximum = num
            result.append(maximum)
        return result
    def findMinimum(self, nums) -> list[int]:
        minimum = float('inf')
        result = []
        for num in nums:
            if minimum > num:
                minimum = num
            result.append(minimum)
        return result
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minimum = self.findMinimum(reversed(nums))
        maximum = self.findMaximum(nums)
        # length = len(nums)
        for index in range(len(nums)):
            score = maximum[index] - minimum[len(nums) - 1 - index]
            if score <= k:
                return index
        return -1