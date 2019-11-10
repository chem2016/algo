def numberOfWaysToMakeChange(n, denoms):
    pass

    """
    if demon <= amount:
        ways[amount] += ways[amount - demon]
    """

    ways = [0 for amount in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]
    

sample_input = 6
sample_input_2 = [1,5]



print(numberOfWaysToMakeChange(6, [1, 5]))
sample_output = 2