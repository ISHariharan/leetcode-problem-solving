class Solution:
    def createSubsets(self, result : List[int], nums : List[int], n:int, length : int) -> List[int]:
        if n == (1 << length):
            return result
        subset = []
        for i in range(length):
            if n & (1 << i):
                subset.append(nums[i])
        result.append(subset)
        return self.createSubsets(result, nums, n + 1, length)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        return self.createSubsets(result, nums, 0, len(nums))