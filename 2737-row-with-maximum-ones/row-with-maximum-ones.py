class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = 0
        least_index =  0
        max_count = 0
        for row in mat:
            one_count = row.count(1)
            if((max_count < one_count)):
                least_index = index
                max_count = one_count 
            index += 1
        return [least_index, max_count]