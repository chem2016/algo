class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == None or len(s) == 0:
            return 0
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        fullString = True
        for c in s:
            if count[ord(c) - ord('a')] < k:
                fullString = False
        if fullString:
            return len(s)
        
        begin, end, result = 0, 0, 0
        
        while end < len(s):
            if count[ord(s[end]) - ord('a')] < k:
                result = max(result, self.longestSubstring(s[begin:end], k))
                begin = end + 1
            end += 1
        
        result = max(result, self.longestSubstring(s[begin:], k))
        
        return result 