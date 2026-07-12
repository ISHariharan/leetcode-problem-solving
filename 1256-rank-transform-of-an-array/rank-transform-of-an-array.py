class Solution:
    def arrayRankTransform(self, arr: List[int]) -> any:
        sortedArr = sorted(arr)
        mapping = {}
        length = len(arr)
        rank = 1
        for index in range(length):
            mapping[sortedArr[index]] = rank
            if not (index + 1 != length and sortedArr[index] == sortedArr[index + 1]):
                rank += 1
        result = []
        for index in range(length):
            result.append(mapping[arr[index]])
        return result
