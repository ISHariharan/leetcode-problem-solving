class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while (n <= 100):
            if n < 10 and n % t == 0:
                return n
            elif n >= 10:
                temp = str(n)
                prod = int(temp[0]) * int(temp[1])
                if prod % t == 0:
                    return n
            n += 1
        return 0
                
        