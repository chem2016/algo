import sys
# class Solution:
#     """
#     @param num: Given the candidate numbers
#     @param target: Given the target number
#     @return: All the combinations that sum to target
#     """
#     def __init__(self):
#         pass
#     def combinationSum2(self, num, target):
#         # write your code here
#         self.result = []
#         self.visited = {}
#         num.sort()
#         self.dfs(0, [], num, target)

#         return self.result

#     def dfs(self, index, tmp, num, target):
        
#         if sum(tmp) == target:
#             to_add_tmp = sorted(tmp[:])
#             if str(to_add_tmp) not in self.visited:
#                 self.result.append(to_add_tmp)
#                 self.visited[str(to_add_tmp)] = True

#         i = index
#         while i < len(num):
#             tmp.append(num[i])
#             self.dfs(index+1, tmp, num, target)
#             tmp.pop()
#             i += 1


class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        if num == None:
            return []
        if len(num) == 0:
            return []
        
        self.result = []
        self.dfs(0, [], sorted(num), target)
        
        return self.result
        
    def dfs(self, index, combination, candidates, target):
        if target == 0:
            self.result.append(combination[:])
            return
        
        for i in range(index, len(candidates)):        
            if i != index and candidates[i-1] == candidates[i]:
                continue
            if candidates[i] > target:
                break
            combination.append(candidates[i])
            print("combination: ", combination)
            self.dfs(i+1, combination, candidates, target-candidates[i])
            combination.pop()

solution = Solution()
result = solution.combinationSum2([7,1,2,5,1,6,10], 8)
print(result)