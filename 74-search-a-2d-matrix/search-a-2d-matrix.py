class Solution:
    def binarySearch(self, row: List[int], target: int) -> bool:
        low = 0
        high = len(row) - 1
        if(low == high):
            if(row[low] == target):
                return True
        while(low <= high):
            mid = (low + high) // 2
            
            if(row[mid] == target):
                return True
            if(row[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            temp = self.binarySearch(row, target)
            if(temp == True):
                break
        return temp