import math

class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        low = 0
        length = len(arr)
        high = length - 1

        while(low <= high):
            mid = math.floor((low + high) / 2)

            if(arr[mid] == target):
                return True
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            elif(arr[low] <= arr[mid]):
                if((arr[low] <= target) and (target <= arr[mid])):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if((arr[mid] <= target) and (target <= arr[high])):
                    low = mid + 1
                else:
                    high = mid - 1
        return False