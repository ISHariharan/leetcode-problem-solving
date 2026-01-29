import math

class Solution:
    def ReqTiming(self, piles: List[int], mid: int) -> int:
        totalTimings = 0
        for i in piles:
            temp = i / mid
            fractional, integer = math.modf(temp)
            if(fractional):
                totalTimings += integer + 1
            else:
                totalTimings += integer
        return int(totalTimings)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        x = max(piles)
        low = 1
        high = x
        lowest = x

        while(low <= high):
            mid = (low + high) // 2
            reqTiming = self.ReqTiming(piles, mid)
            if(reqTiming <= h and mid <= lowest):
                lowest = mid
            if(reqTiming > h):
                low = mid + 1
            else:
                high = mid - 1
        return lowest