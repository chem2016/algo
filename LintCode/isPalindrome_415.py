class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        
        # isalnum() return true is a char is alphanumeric
        # convert to an array contains only alphanumeric
        alphanumeric_arr = []
        for char in s:
            if char.isalnum():
                alphanumeric_arr.append(char.lower())
                
        # edge cases
        if len(s) == 0:
            return True
        elif len(alphanumeric_arr) == 1:
            return True
        else:
            left = 0
            right = len(alphanumeric_arr) - 1
            if len(alphanumeric_arr) % 2 == 1:
                while(left <= int(len(alphanumeric_arr)/2)):
                    if alphanumeric_arr[left] != alphanumeric_arr[right]:
                        return False
                    else:
                        left += 1
                        right -= 1
            else:
                while(left <= int(len(alphanumeric_arr)/2) -1):
                    if alphanumeric_arr[left] != alphanumeric_arr[right]:
                        return False
                    else:
                        left += 1
                        right -= 1
            return True
            
            
    