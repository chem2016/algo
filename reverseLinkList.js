const mkNode = (value, next = null) => ({ value, next })
const nums = mkNode(1, mkNode(2, mkNode(3)))
const nums2 = mkNode(3)

// log values in reverse order
// const logReversed = list => {
//     console.log("coming in list: ", list)
//     if (!list) return
//     logReversed(list.next)
//     console.log("list, list.value: ", list, list.value)
// }

// return a reversed linklist
// const reverse = initList => {
//     const go = (oldList, newList) => {
//         if (!oldList) return newList
//         const newerList = mkNode(oldList.value, newList)
//         return go(oldList.next, newerList)
//     }
//     return go(initList, null)
// }

// const reverse = (oldList, newList = null) => {
//     if (!oldList) return newList
//     const newerList = mkNode(oldList.value, newList)
//     return reverse(oldList.next, newerList)
// }


function logReversed(nums){
    if(!nums) return 
    const temp = nums.next
    console.log(logReversed(temp))
}

logReversed(nums)
// logReversed(nums2)
// const numsR = reverse(nums)
// console.log(nums)
// console.log(numsR)

