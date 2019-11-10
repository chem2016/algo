def powerset(array):
    # Write your code here.
    ret_arr = [[]]
    for ele1 in array:
        for i in range(len(ret_arr)):  # use index to prevent to go all the way
            current_set = ret_arr[i]
            ret_arr.append(current_set + [ele1])

    return ret_arr

print(powerset([1,2,3]))

