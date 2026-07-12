class Solution:
    def arrayRankTransform(self, arr: List[int]) -> any:
        sortedArr = sorted(set(arr))
        mapping = {}
        length = len(arr)
        rank = 1
        for items in sortedArr:
            mapping[items] = rank
            rank += 1
        result = []
        for index in range(length):
            result.append(mapping[arr[index]])
        return result
