class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals)
        length = len(intervals)
        index = 0
        while index < length-1:
            if sortedIntervals[index][0] <= sortedIntervals[index+1][0] and sortedIntervals[index+1][1] <= sortedIntervals[index][1]:
                del sortedIntervals[index + 1]
                length = len(sortedIntervals) 
            elif sortedIntervals[index+1][0] <= sortedIntervals[index][0] and sortedIntervals[index][1] <= sortedIntervals[index+1][1]:
                del sortedIntervals[index]
                length = len(sortedIntervals) 
            else:
                index += 1
        return len(sortedIntervals)