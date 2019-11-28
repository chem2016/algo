class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def __init__(self, s):
        self.s = s

    def longestPalindrome(self):
        # write your code here
        s = self.s
        # write your code here
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        else:
            letters_dict = {}
            longest = 0
            for char in s:
                if char in letters_dict.keys():
                    letters_dict[char] += 1
                else:
                    letters_dict[char] = 1
            
            has_odd = False
            for key, value in letters_dict.items():
                if value % 2 == 0:
                    longest += value
                else:
                    has_odd = True
                    longest += 2*(int(value / 2))
            
            return longest + 1 if has_odd else longest  


ret = Solution('abccccdd')
# print(ret.longestPalindrome('abcccdd'))
length = ret.longestPalindrome()
print(length)