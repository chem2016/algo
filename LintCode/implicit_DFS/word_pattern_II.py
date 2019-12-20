class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        Hashmap = {}
        return self.dfs(Hashmap, pattern, str)
        
    def dfs(self, Hashmap, pattern, str):
        # if one is at the end the other still not finish means no match
        if len(pattern) == 0 and len(str) == 0:
            return True
        if len(pattern) == 0 or len(str) == 0:
            return False
        
        # always start at the beginning and dfs into the next one
        c = pattern[0]
        
        # if the char we are looking at alreay in Hashmap, we check the remaining str startswith that word
        if c in Hashmap:
            word = Hashmap[c]
            if not str.startswith(word):
                return False
            else:
                # check the next letter in pattern and remaining str
                return self.dfs(Hashmap, pattern[1:], str[len(word):])
        
        # if the char in not yet in our Hashmap, we need to try all the combinations of str. from 0->1, 0->2, etc
        for i in range(0, len(str)):
            word = str[0:i+1]
            # if the word show up in the value but the c is not. mean there is a value corresponds to two different c
            if word in Hashmap.values():
                continue
            Hashmap[c] = word
            # look onto the next pattern and string
            if self.dfs(Hashmap, pattern[1:], str[i+1:]):
                return True
            del Hashmap[c] # backtracking
        
        return False