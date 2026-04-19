class Solution:
    def returnMax(self, num: int, nums2: List[int], index: int) -> int:
        left = 0
        right = len(nums2) - 1
        maxi = 0
        while (left <= right):
            mid = (left + right) // 2
            if num <= nums2[mid]:
                maxi = max(mid - index, maxi)
                left = mid + 1

            elif nums2[mid] < num:
                right = mid - 1
        return maxi 
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxi = 0
        for index in range(len(nums1)):
            maxi = max(self.returnMax(nums1[index], nums2, index), maxi)
        return maxi