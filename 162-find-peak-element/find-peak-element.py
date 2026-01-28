class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        low = 0
        length = len(arr)
        high = length - 2
        if(length == 1):
            return 0
        if(length == 2):
            if(arr[0] > arr[1]):
                return 0
            else:
                return 1
        while(low <= high):
            mid = (low + high) // 2
            if((arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1])):
                return mid
            elif(arr[mid + 1] > arr[mid]):
                low = mid + 1
            else:
                high = mid - 1
        return length - 1       