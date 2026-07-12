class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length =   len(nums)
        if length == 1:
            return nums[0]
        maxProd = float('-inf')
        prod = 1
        for index in range(length):
            prod *= nums[index]
            maxProd = max(prod, maxProd)
            if prod == 0:
                prod = 1
        prod = 1
        for index in range(length - 1, -1, -1):
            prod *= nums[index]
            maxProd = max(prod, maxProd)
            if prod == 0:
                prod = 1
        return maxProd