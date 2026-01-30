import math

class Solution:
    def Quotient_Sum(self,  nums: List[int], divisor: int) -> int:
        total = 0
        for i in nums: 
            temp = i / divisor
            fractional, integer = math.modf(temp)
            if(fractional):
                total += integer + 1
            else:
                total += integer
        return total
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        length = len(nums)
        max_value = max(nums)
        if threshold == nums:
            return max_value
        
        low = 1
        high = max_value
        smallest = math.inf

        while(low <= high):
            mid = (low + high) // 2
            sum_of_quotient = self.Quotient_Sum(nums, mid)

            if((sum_of_quotient <= threshold) and (mid <= smallest)):
                smallest = mid

            if(sum_of_quotient > threshold):
                low = mid + 1
            else: 
                high = mid - 1
        return smallest
        