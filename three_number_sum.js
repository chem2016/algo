function threeNumberSum(array, targetSum) {
    // Write your code here.
      const retArr = [];
      const myArr = array.sort((a, b)=> {return a-b})
      // myArr:-8,-6,1,2,3,5,6,12
      for(let i = 0; i < myArr.length - 2; i++){
          let left = i+1;
          let right = myArr.length - 1;
          while(left < right){
              if(myArr[i] + myArr[left] + myArr[right] === targetSum){
                  retArr.push([myArr[i], myArr[left], myArr[right]])
                  left += 1;
                  right -= 1;
              }else if(myArr[i] + myArr[left] + myArr[right] < targetSum){
                  left += 1;
              }else{
                  right -= 1;
              }
          }
      }
      return retArr;
  }
  