// function longestIncreasingSubsequence (sequence, idx = 0, base = -Infinity) {
//   if (idx === sequence.length) return 0;
//   const num = sequence[idx];
//   const whenExcluded = longestIncreasingSubsequence(sequence, idx + 1, base);
//   if (num <= base) return whenExcluded;
//   const whenIncluded = 1 + longestIncreasingSubsequence(sequence, idx + 1, num);
//   return Math.max(whenIncluded, whenExcluded);
// }

// n^2 method // space O(n)
function longestIncreasingSubsequence(sequence){
  if (sequence.length === 1) return 1;
  let lengths = new Array(sequence.length).fill(1);

  for (let i = 1; i < sequence.length; i++){
    for (let j = 0; j < i; j++){
      const isIncreasing = sequence[j] < sequence[i];
      const sequenceLength = lengths[j] + 1
      const isLonger = sequenceLength > lengths[i]
      if (isIncreasing && isLonger){
        lengths[i] = sequenceLength;
      }
    }
  }
  return Math.max(...lengths);
}
function findLongestPrefixLength (currentIndex) { // binary search, O(log n)
  let low = 1;
  let high = 0;
  
  while (low <= high) {
    const mid = Math.ceil((low + high) / 2);
    if (sequence[lastIndicesOfSubByLength[mid]] < sequence[currentIndex]) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  
  // after searching, low is 1 greater than the length of the longest *prefix* of `sequence[currentIndex]`
  return low - 1;
}


function longestIncreasingSubsequence (sequence) {
  let maxSubLength = 0;
  
  // Let lastIndicesOfSubByLength[pos] be defined as the smallest integer (by index) that ends an increasing subsequence of length `pos`
    // So we are keeping track of the index at which the longest subsequence of a given length terminates 
    // i.e. with the subsequence 1,3,5, if 5 is found at index 9, then index 3 (the length) would store the value 9 (lastIndicesOfSubByLength[3] = 9)
  const lastIndicesOfSubByLength = [];
  
  // keep track of predecessors if you want to regenerate and return the actual subsequence
    // `predecessors` will be equal in length to `sequence`
    // Each `i` will correspond to the index of the predecessor of `sequence[i]`
  const predecessors = [];
  
  for (let i = 0; i < sequence.length; i++) { // O(n)
    // find the length of the longest prefix that terminates with a number less than the current one
    const longestPrefixLength = findLongestPrefixLength(i);
    // add one to include our current one
    const longestAtCurrentIndex = longestPrefixLength + 1;
    
    if (longestAtCurrentIndex > maxSubLength) {
      maxSubLength = longestAtCurrentIndex;
    }
    
    lastIndicesOfSubByLength[longestAtCurrentIndex] = i;

    predecessors[i] = lastIndicesOfSubByLength[longestAtCurrentIndex - 1];
  } 
  
  const subsequence = [];
  let currentSubsequenceIndex = lastIndicesOfSubByLength[maxSubLength];
  
  for (let i = maxSubLength - 1; i >= 0; i--) {
    subsequence[i] = sequence[currentSubsequenceIndex];
    // reassign the index we are looking at based on predecessor array
    currentSubsequenceIndex = predecessors[currentSubsequenceIndex];
  }
  
  return subsequence;

}
console.log(longestIncreasingSubsequence([3, 4, 2, 1, 10, 6]));
// should return 3, the length of the longest increasing subsequence:
// 3, 4, 6 (or 3, 4, 10)
console.log(longestIncreasingSubsequence([10, 22, 9, 33, 20, 50, 41, 60, 80]));
// should return 6, the length of the maximum increasing subsequence:
// 10, 22, 33, 41, 60, 80 (or 10, 22, 33, 50, 60, 80)
console.log(longestIncreasingSubsequence([10, 22, 9, 33, 20, 50, 41, 60, 80, 21, 23, 24, 25, 26, 27, 28]));
// should return 9, the length of the maximum increasing subsequence:
// 10, 20, 21, 23, 24, 25, 26, 27, 28
