function recursiveStringPermutations(str) {
    var results = [];
    getPerms(str, []);
    function getPerms(str, arr) {
      if (typeof str === 'string')
        //on first call, split the string into an array
        str = str.split('');
      if (!str.length)
        //base case- push the compiled results into the results variable
        results.push(arr.join(''));
      for (var i = 0; i < str.length; i++) {
        var letter = str.splice(i, 1);
        // console.log('letter: ', letter)
        arr.push(letter);
        getPerms(str, arr); //recursive call
        arr.pop();
        str.splice(i, 0, letter);
      }
    }
    return results
      .filter(function(el, index) {
        // console.log(results)
        return results.indexOf(el) === index; //filter out non-unique words
      })
      .sort();
  }

  const perms = recursiveStringPermutations('abcd');
//   console.log(perms)

//   const a = '0123456'.slice(2, 1)
//   console.log(a)
//   a = ['ab', 'bc', 'ab']
//   a.filter(function(el, index) {
//     console.log(el, index, a.indexOf(el))
//     return a.indexOf(el) === index; //filter out non-unique words
//   })

//   console.log(a)

let str = 'abcd'.split('')
console.log(str)
for (var i = 0; i < str.length; i++) {
    console.log(i, str.length)
    var letter = str.splice(i, 1);
    console.log(i, letter)
}