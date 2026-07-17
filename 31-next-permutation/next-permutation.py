from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = - 1
        length = len(nums)
        for index in range(length - 2, -1, -1):
            if nums[index] < nums[index + 1]:
                ind = index
                break
        if ind == -1:
            return nums.reverse()
        for index in range(length - 1, -1, -1):
            if nums[index] > nums[ind]:
                nums[ind], nums[index] = nums[index], nums[ind]
                break
        nums[ind + 1: length] = nums[ind + 1: length][::-1]
        return nums
        