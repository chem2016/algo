# dynamic programming, solve small problems and gradually build
# up the final answer

def minNumberOfCoinForChange(n, demons):
    """
    A function to return the minimum number of coin to 
    make the target n amount
    """
    # n -> [0, 1, 2, 3, 4, 5, ..., n]
    # numbers[0] = 0, numbers[1] = inf, etc
    # numbers[amount] = min(numbers[amount], numbers[amount - demon]+1)
    # logic is 0, 1, 2, 3, 4, 5, 6, 7
    # using demon = 1
    # nums     0, 1, 2, 3, 4, 5, 6, 7
    # using demon = 2
    # nums     0, 1, 1, 2, 2, 3, 3, 4
    # using demon = 5
    # nums     0, 1, 1, 1, 1, 1, 2, 2

    numbers = [float('Inf') for number in range(n+1)]
    numbers[0] = 0
    for demon in demons:
        for amount in range(n+1):
            if demon <= amount:
                numbers[amount] = min(numbers[amount], numbers[amount - demon] + 1)
    
    return numbers[n] if numbers[n] != float('Inf') else -1 

sample_input = 11
demons = [1, 2, 5]
sample_output = 3

print(minNumberOfCoinForChange(sample_input, demons))
print("expected output is: ", 3)