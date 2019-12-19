class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        
        # edge cases:
        if digits == None:
            return []
        if len(digits) == 0:
            return []
        
        self.dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.result = []
        # dfs
        self.dfs(0, [], digits)
        
        return self.result
        
    def dfs(self, index, tmp, digits):
        
        if len(tmp) == len(digits):
            self.result.append("".join(tmp))
            return
        for char in self.dict[digits[index]]:
            tmp.append(char)
            self.dfs(index+1, tmp, digits)
            tmp.pop()