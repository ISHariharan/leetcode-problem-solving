import math

class Solution:
    def computeLeftMax(self, height : List[int], length: int) -> List[int]:
        maxiLeftArr = [0] * length
        maxiLeftArr[0] = height[0]
        for position in range(1, length):
            maxiLeftArr[position] = max(maxiLeftArr[position - 1], height[position])
        return maxiLeftArr 
    def computeRightMax(self, height : List[int], length: int) -> List[int]:
        maxiRightArr = [0] * length
        maxiRightArr[length - 1] = height[length - 1]
        for position in range(length - 2, -1, -1):
            maxiRightArr[position] = max(maxiRightArr[position + 1], height[position])
        return maxiRightArr
    def trap(self, height: List[int]) -> int:
        totalSaved = 0
        length = len(height)
        leftMaxArr = self.computeLeftMax(height, length)
        rightMaxArr = self.computeRightMax(height, length)
        for position in range(0, length):
            savedWater = min(leftMaxArr[position], rightMaxArr[position]) - height[position]
            if savedWater > 0:
                totalSaved += savedWater
        return totalSaved