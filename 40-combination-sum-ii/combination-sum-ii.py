class Solution:
    def findCombinations(self, candidates, ans, target, temp, index, length):
        if target == 0:
            ans.append(temp[:])
            return
        if index >= length:
            return
        
        if candidates[index] <= target:
            ## picking
            temp.append(candidates[index])
            self.findCombinations(candidates, ans, target - candidates[index], temp, index + 1, length)

            ## Not Picking
            temp.pop()
        while index + 1 < length and candidates[index] == candidates[index + 1]:
            index += 1
        self.findCombinations(candidates, ans, target, temp, index + 1, length)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # if len(set(candidates)) == 1 and len(candidates) >= target / list(set(candidates))[0] and len(candidates) > 3:
        #     return [[list(set(candidates))[0]] * (target // list(set(candidates))[0])]
        ans = []
        candidates = sorted(candidates)
        self.findCombinations(candidates, ans, target, [], 0, len(candidates))
        return ans