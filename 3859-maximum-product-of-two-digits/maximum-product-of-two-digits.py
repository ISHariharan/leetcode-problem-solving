class Solution:
    def maxProduct(self, n: int) -> int:
        maxProd = 0
        sen = str(n)
        length = len(sen)
        for i in range(length):
            for j in range(i + 1,length):
                maxProd = max(maxProd, int(sen[i]) * int(sen[j]))
        return maxProd