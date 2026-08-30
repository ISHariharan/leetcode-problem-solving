class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 1
        maxiIndex = nums.index(max(nums))
        miniIndex = nums.index(min(nums))
        removed, removingFromFirst, removingFromLast = 0, 0, 0
        if length % 2 == 0:
            mid = length // 2
        elif length % 2 == 1:
            mid = ((length // 2) + ((length + 1) // 2)) // 2
        if maxiIndex <= mid and miniIndex <= mid:
            if maxiIndex < miniIndex:
                removed = miniIndex + 1
                removingFromFirst = miniIndex + 1
                removingFromLast = length - maxiIndex
            else:
                removed = maxiIndex + 1
                removingFromFirst = maxiIndex + 1
                removingFromLast = length - miniIndex
        elif maxiIndex >= mid and miniIndex >= mid:
            if maxiIndex < miniIndex:
                removed =  length - maxiIndex
                removingFromFirst = miniIndex + 1
                removingFromLast = length - maxiIndex
            else:
                removed =  length - miniIndex
                removingFromFirst = maxiIndex + 1
                removingFromLast = length - miniIndex
        else:
            if maxiIndex < miniIndex:
                removed = (maxiIndex + 1) + (length - miniIndex)
                removingFromFirst = miniIndex + 1
                removingFromLast = length - maxiIndex
            else:
                removed = (miniIndex + 1) + (length - maxiIndex)
                removingFromFirst = maxiIndex + 1
                removingFromLast = length - miniIndex
        return min(removed, removingFromFirst, removingFromLast)
