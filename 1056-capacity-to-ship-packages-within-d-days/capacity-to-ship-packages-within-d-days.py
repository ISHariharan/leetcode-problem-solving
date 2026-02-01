import math

class Solution:
    def weights_to_days(self, weights: List[int], days: int) ->int:
        total_days = 0
        temp = 0
        for i in weights: 
            temp += i
            if(temp > days):
                total_days += 1
                temp = i
        if temp > 0:
            total_days += 1
        return total_days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        least_capacity = math.inf

        while(low <= high):
            mid = (low + high) // 2
            total_days = self.weights_to_days(weights, mid)

            if((total_days <= days) and (mid <= least_capacity)):
                least_capacity = mid
            
            if(total_days > days):
                low = mid + 1
            else:
                high = mid - 1
        return least_capacity