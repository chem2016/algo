function binarySearch(arr, target){
    if(arr.length < 1) return -1;
    let start = 0;
    let end = arr.length - 1;
    while(start + 1 < end){
        let mid = Math.floor((start + end) / 2);
        if(arr[mid] < target){
            start = mid
        }else if(arr[mid] == target){
            end = mid
        }else{
            end = mid
        }
    }
    if(arr[start] == target){
        return start
    }
    if(arr[end] == target){
        return end
    }
    return -1
}

const match = binarySearch([1,3,4,7,12,17,17,17,20], 17)
// const match = binarySearch([1,1], 1)
console.log('position is: ', match)