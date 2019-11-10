
def searchInSortedMatrix(matrix, target):
    # Write your code here.
	# start from right upper corner and then zigzag to the find the right answer
	i = 0
	j = len(matrix[0]) - 1
	while(i <= len(matrix) - 1 and j >= 0):
		if matrix[i][j] > target:
			j = j - 1
		elif matrix[i][j] < target:
			i = i + 1
		else:
			return [i, j]
	return [-1, -1]
	

# def searchInSortedMatrix(matrix, target):
#     for i in range(len(matrix)):
#         # for j in range(len(matrix[i])): # this scales O(n2)
#         #     if matrix[i][j] == target:
#         #         return [i, j]
#         j = searchInSortedArray(matrix[i], target)  # this scales O(nlog(n))
#         if j != -1:
#             return [i, j]
#     return [-1,-1]

# def searchInSortedArray(array, target):
    
#     middle_index = int(len(array) / 2)
    
#     while middle_index > 0:
#         if array[middle_index] > target:
#             middle_index = int((middle_index + len(array) - 1)/2)
#         elif array[middle_index] < target:
#             middle_index = int((middle_index + 0)/2)
#         else:
#             return middle_index

#     return -1

# sample_input = [
#     [1,4,7,12,15,1000],
#     [2,5,19,31,32,1001],
#     [3,8,24,33,35,1002],
#     [40,41,42,44,45,1003],
#     [99,100,103,106,128,1004],
# ]

# target = 44

# print('expected results: ')
# print(searchInSortedMatrix(sample_input, target))

# print(searchInSortedArray([3,8,24,33,35,1002],44))
# print(searchInSortedArray([40,41,42,44,45,1003],44))