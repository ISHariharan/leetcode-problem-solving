class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        length = len(nums)
        lowest = nums[0] + 1
        highest = nums[length - 1]
        index = 1
        missing = []
        while lowest <= highest and index < length:
            if lowest < nums[index]:
                missing.append(lowest)
            elif lowest == nums[index]:
                index += 1
            lowest += 1
        return missing
        