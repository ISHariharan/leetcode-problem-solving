class Solution:
    def __init__(self):
        self.ans = []
    def findCombinations(self, arr, targetLength, length, target, temp, index):
        if target == 0 and targetLength == len(temp):
            self.ans.append(temp.copy())
            return
        if index >= length:
            return
        if arr[index] <= target:
            temp.append(arr[index])
            self.findCombinations(arr, targetLength, length, target - arr[index], temp, index + 1)

            temp.pop()
        self.findCombinations(arr, targetLength, length, target, temp, index + 1)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1,2,3,4,5,6,7,8,9]
        self.findCombinations(arr, k, len(arr), n, [], 0)
        return self.ans