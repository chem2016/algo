// def powerset(array):
//     # Write your code here.
//     ret_arr = [[]]
//     for ele1 in array:
//         for i in range(len(ret_arr)):  # use index to prevent to go all the way
//             current_set = ret_arr[i]
//             ret_arr.append(current_set + [ele1])

//     return ret_arr

// print(powerset([1,2,3]))


function powerset(array){
    const retArr = [[]];
    for(let i = 0; i < array.length; i++){
        console.log(i)
        retArr_copy = [...retArr]
        for(let j = 0; j < retArr_copy.length; j++){
            console.log(j)
            currentSet = retArr[j]
            newSet = [...currentSet, array[i]]
            retArr.push(newSet)
        }
    }
    return retArr;
}
powerset([1,2,3])
// console.log(powerset([1,2,3]))