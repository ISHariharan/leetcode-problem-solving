class Solution:
    def maxProduct(self, n: int) -> int:
        arr = sorted(str(n))
        length = len(arr)
        if length == 1:
            return 0
        return int(arr[length - 1]) * int(arr[length - 2])