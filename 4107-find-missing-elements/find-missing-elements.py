class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        length = len(nums)
        lowest = nums[0]
        highest = nums[length - 1]
        missing = []
        for num in range(lowest, highest + 1):
            if num not in nums:
                missing.append(num)
        return missing
        