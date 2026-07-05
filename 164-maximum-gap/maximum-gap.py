class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(nums)
        if length < 2 : 
            return 0
        i = 0
        j = 1
        maxDiff = 0
        while (j < length):
            diff = nums[j] - nums[i]
            maxDiff = max(diff, maxDiff)
            i += 1
            j += 1
        return maxDiff