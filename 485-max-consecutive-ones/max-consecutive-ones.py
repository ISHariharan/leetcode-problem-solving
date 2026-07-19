class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = -1
        for num in nums:
            if num != 1 and count > maxi:
                maxi = max(maxi, count)
                count = 0
            elif num != 1:
                count = 0
            elif num == 1:
                count +=1
        if count != 0 and count > maxi:
            return count
        return maxi