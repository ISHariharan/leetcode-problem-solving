import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        length = len(nums)
        high = length - 1
        lowest = math.inf
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] < lowest):
                lowest = nums[mid]
            elif(nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid - 1
        return lowest
