class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        numbers = str(n)
        summation = 0
        revised_number = ""
        for number in numbers :
            if number != '0':
                revised_number += number
                summation += int(number)
        return int(revised_number) * summation