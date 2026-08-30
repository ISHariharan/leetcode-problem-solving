class Solution:
    def findCombinations(self, candidates, index, length, target, temp, ans):
        if target == 0:
            ans.append(temp.copy())
            return
        if index >= length:
            return
        
        if candidates[index] <= target:
            temp.append(candidates[index])
            self.findCombinations(candidates, index, length, target-candidates[index], temp, ans)

            ## if we are not picking
            temp.pop()
        self.findCombinations(candidates, index + 1, length, target, temp, ans)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.findCombinations(candidates, 0, len(candidates), target, [], ans)
        return ans