import math

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        highest = float('-inf')

        if(x == 0):
            return 0

        while(low <= high):
            mid = (low + high) // 2
            square = mid * mid
            if(square <=x and mid >= highest):
                highest = mid
            if(square < x):
                low = mid + 1
            else:
                high = mid - 1
        return highest