class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 0
        for digit in digits:
            add = add*10 + digit 
        List = list(map(int, list(str(add + 1))))
        return List