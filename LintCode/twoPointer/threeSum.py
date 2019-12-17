class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        result = []
        result_set = set()
        for i in range(0, len(numbers)-2):
            left, right = i+1, len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] + numbers[i] < 0:
                    left += 1
                elif numbers[left] + numbers[right] + numbers[i] > 0:
                    right -= 1
                else:
                    if str([numbers[i], numbers[left], numbers[right]]) in result_set:
                        left += 1
                        right -= 1
                        continue
                    else:
                        result_set.add(str([numbers[i], numbers[left], numbers[right]]))
                        result.append([numbers[i], numbers[left], numbers[right]])
                        left += 1
                        right -= 1
                    
        return result

solution = Solution()
result = solution.threeSum([-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5])
print(result)