def riverSizes(matrix):
    size = []
    # use an auxilary matrix to keep track of visited nodes
    visited = [[ False for ele in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, size)
    
    return size
   
def traverseNode(i, j, matrix, visited, size):

    nodesToExplore = [[i, j]]
    currentRiverSize = 0
    while(len(nodesToExplore)):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        size.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):

    unvisitedNeighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisitedNeighbors.append([i, j+1])

    return unvisitedNeighbors

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

print(riverSizes(matrix))
print("expected output: ", [1,2,2,2,5])