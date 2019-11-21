const generatePermutations = (word)=>{
    const letters = word.split('');
    let letter = letters.shift();
  
    let results = [[letter]];
    while(letters.length){
      letter = letters.shift();
      const _results = [];
      results.forEach( perm => {
          console.log('perm: ', perm)
          for(let i = 0; i <= perm.length; i++){
              console.log("i: ", i)
              const copy = [...perm];
              copy.splice(i, 0, letter);
              console.log(copy)
              _results.push(copy);
            }
        });
       results = _results;
    //    console.log(_results)
    }
    return results;
  }
  
  const perms = generatePermutations('abcd');
//   perms.forEach(p => console.log(p));
  console.log(perms.length);


  function stringPermutations(str) {
    var results = [];
    var letters = str.split('');
    results.push([letters.shift()]); //add first letter (as an array) to results
    while (letters.length) {
      var curLetter = letters.shift();
      var tmpResults = [];
      results.forEach(function(curResult) {
        for (var i = 0; i <= curResult.length; i++) {
          var tmp = curResult.slice(); //make copy so we can modify it
          //insert the letter at the current position
          tmp.splice(i, 0, curLetter);
          tmpResults.push(tmp);
        }
      });
      results = tmpResults; //overwrite the previous results
    }
    return results
      .map(function(letterArr) {
        return letterArr.join('');
      })
      .filter(function(el, index, self) {
        return self.indexOf(el) === index; //filter out non-unique words
      })
      .sort();
  }

  