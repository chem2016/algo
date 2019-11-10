def findIsland(i, j, matrix):
    """
    A function to find edges of a island
    """
    visited = [[ False for ele in row] for row in matrix]
    totalEdges = traverseNodes(i, j, matrix, visited)

    return totalEdges

def traverseNodes(i, j, matrix, visited):
    nodesToExplore = [[i, j]]
    totalEdges = 0

    while(len(nodesToExplore)):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        # logic of adding edges here
        if matrix[i][j] == 0:
            continue
        numberToAdd = calculateEdges(i, j, matrix)
        totalEdges += numberToAdd
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    return totalEdges 

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

def calculateEdges(i, j, matrix):
    """
    A function that returns the number of edges base on neighbors
    """
    num = 0
    if i > 0:
        if matrix[i-1][j] == 0:
            num += 1
    if j > 0:
        if matrix[i][j-1] == 0:
            num += 1
    if i < len(matrix) - 1:
        if matrix[i+1][j] == 0:
            num += 1
    if j < len(matrix[0]) - 1:
        if matrix[i][j+1] == 0:
            num += 1
    
    return num

matrix = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

i, j = 2, 2

print(findIsland(i, j, matrix))