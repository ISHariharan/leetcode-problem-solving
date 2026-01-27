class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        length = len(arr)
        if(length == 1):
            return arr[0]
        if(arr[0] != arr[1]):
            return arr[0]
        if(arr[length - 1] != arr[length-2]):
            return arr[length - 1]
        low = 1
        high = length - 2
        while(low <= high):
            mid = (low + high) // 2
            if((arr[mid] != arr[mid - 1]) and (arr[mid]  != arr[mid + 1])):
                return arr[mid]
            elif(((mid %2 == 0) and (arr[mid] == arr[mid - 1])) or ((mid %2 == 1) and (arr[mid] == arr[mid + 1]))):
                high = mid - 1
            else:
                low = mid + 1
        return -1