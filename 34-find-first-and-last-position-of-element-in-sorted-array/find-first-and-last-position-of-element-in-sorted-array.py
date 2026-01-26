import math
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            first = nums.index(target)
            nums.reverse()
            last = len(nums) - 1 - nums.index(target)
            return [first, last]
        except:
            return [-1,-1]

        