class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        rowLen = len(grid)
        colLen = len(grid[0])
        for row in range(rowLen):
            for col in range(colLen):
                nums.append(grid[row][col])
        length = len(nums)
        k = k % length
        arr = nums[length - k: length]
        del nums[length - k: length]
        nums = arr + nums
        index = 0
        for row in range(rowLen):
            for col in range(colLen):
                grid[row][col] = nums[index]
                index +=1
        return grid