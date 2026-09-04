class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for index in range(len(nums)):
            score = max(nums[:index + 1]) - min(nums[index:])
            if score <= k:
                return index
        return -1