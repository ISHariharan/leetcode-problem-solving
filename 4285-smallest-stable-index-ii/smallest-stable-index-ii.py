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
        # minimum, maximum = [], []
        minimum = self.findMinimum(reversed(nums))
        maximum = self.findMaximum(nums)
        right = len(nums)
        for index in range(right):
            score = maximum[index] - minimum[right - 1 - index]
            if score <= k:
                return index
        return -1