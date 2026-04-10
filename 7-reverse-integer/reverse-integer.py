import math

class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            string = (str(x)[1:])[::-1]
            x = 0 - int(string)
            in_range = -2**31 <= x <= 2**31 - 1
            if not in_range:
                return 0
            return x
        x = int(str(x)[::-1])
        in_range = -2**31 <= x <= 2**31 - 1
        if not in_range:
            return 0
        return x
