class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        arr1Len = 0
        arr2Len = 0
        for num in nums:
            if arr1 == []:
                arr1.append(num)
                arr1Len += 1
                continue
            elif arr2 == []:
                arr2.append(num)
                arr2Len += 1
                continue
            else:
                if arr1[arr1Len - 1] > arr2[arr2Len - 1]:
                    arr1.append(num)
                    arr1Len += 1
                elif arr1[arr1Len - 1] < arr2[arr2Len - 1]:
                    arr2.append(num)
                    arr2Len += 1
        arr1.extend(arr2)
        return arr1