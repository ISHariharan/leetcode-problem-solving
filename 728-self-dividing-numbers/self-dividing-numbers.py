class Solution:
    def checkSelfDividingNumber(self, num : int):
        if num % 10 == 0:
            return False
        string = str(num)
        if '0' in string:
            return False
        for char in string:
            if num % int(char) != 0:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if(self.checkSelfDividingNumber(num)):
                result.append(num)
        return result