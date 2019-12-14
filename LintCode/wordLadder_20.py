import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def __init__(self):
        pass

    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        distance = 0
        visited = set([start])
        # BFS
        while(queue):
            currentWord = queue.popleft()
            distance += 1
            print(currentWord, distance)
            if currentWord == end:
                return distance
            nextWords = self.getNextWord(currentWord, dict)
            for nextWord in nextWords:
                queue.append(nextWord)
    
    def getNextWord(self, word, dict):
        nextWords = []
        for i in range(0, len(word)):
            left, right = word[0:i], word[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[i]:
                    continue
                nextCandidate = left + char + right
                if nextCandidate in dict:
                    nextWords.append(nextCandidate)
        
        return nextWords

solution = Solution()

# result = solution.ladderLength("a", "c", set(["a", "b", "c"]))
result = solution.ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
print(result)