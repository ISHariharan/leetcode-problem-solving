class Solution:
    def binarySearch(self, row, target):
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix, target):
        for row in matrix:
            if self.binarySearch(row, target):
                return True
        return False