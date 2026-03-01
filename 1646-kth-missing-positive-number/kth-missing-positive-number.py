class Solution:
    def createArray(self, start:int, gap: int):
        temp_arr = []
        temp = start
        for num in range(temp, temp + gap):
            temp_arr.append(num);
        return temp_arr;

    def findKthPositive(self, arr: List[int], k: int) -> List[int]:
        index = 0
        length = len(arr)
        start, end = 1, arr[length - 1]
        missing_arr = []
        if(length == arr[length - 1]):
            return arr[length - 1] + k;
        if(length == 1 and arr[0] > k):
            return k;
        while((index < length) and (len(missing_arr) < k)):
            if((index == 0) and (arr[index] - start != 0)):
                missing_arr += self.createArray(start, arr[index] - start);
            else:
                if(arr[index] - arr[index - 1] != 1):
                    missing_arr += self.createArray(arr[index - 1] + 1, arr[index] - arr[index - 1] - 1);
            index += 1
        if(k > len(missing_arr)):
            return arr[length - 1] + k - len(missing_arr)
        return missing_arr[k-1];