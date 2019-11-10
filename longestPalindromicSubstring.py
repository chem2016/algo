# def longestPalindromicSubstring(string):
    
#     longestString = ''
#     for i in range(len(string)):
#         for j in range(len(string)):
#             if j > i:
#                 substring = string[i:j+1]
#                 if isPalindrom(substring):
#                     if len(longestString) < len(substring):
#                         longestString = substring
    
#     return longestString


# def isPalindrom(string):

#     reversed_string = string[::-1]
#     if string == reversed_string:
#         return True
#     else:
#         return False

### beter time scale method:


def longestPalindromicSubstring(string):

    currentLongest = [0,1]
    for i in range(1, len(string)):
        odd = getLongestPalindrom(string, i-1, i+1)
        even = getLongestPalindrom(string, i-1, i)
        longest = max(odd, even, key= lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key= lambda x: x[1] - x[0])

    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindrom(string, leftIdx, rightIdx):

    while(leftIdx >=0 and rightIdx < len(string)):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    
    return [leftIdx + 1, rightIdx]

sample_input = "abaxyzzyxf"
sample_output = "xyzzyx"

print(longestPalindromicSubstring(sample_input))

# better solutions