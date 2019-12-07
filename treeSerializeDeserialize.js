class TreeNode {
  constructor (val) {
    this.val = val
    this.left = null
    this.right = null
  }
}

const serialize = function(root) {
  if (root == null || root.val === undefined) {
    return "{}";
  }

  let result = '';
  let resultArry = []
  let queue = [];

  if (root == null) {
    return result;
  }
  queue.push(root);
  while(queue.length > 0){
    let head = queue.shift();
    if (head !== null && head!== undefined){
      resultArry.push(head.val);
    }else{
      if (queue.length > 0){
        resultArry.push('#');
      }
    }
    if (head !== null && head!== undefined){
      queue.push(head.left);
      queue.push(head.right);
    }
  }
  console.log(resultArry)
  while (resultArry[resultArry.length - 1] == "#") {
    resultArry.pop();
  }
  console.log(resultArry);
  result = `{${resultArry.join(', ')}}`;
  return result;
}

const deserialize = function(data) {
  if (data ==='{}') {
    return null;
  }
  let str = data.slice(1, data.length-1);
  let numArr = str.split(', ');

  let level = 0;
  let isLeftChild = true;

  let root = new TreeNode(numArr[0]);
  let queue = []
  queue.push(root);

  for (let i=1; i<numArr.length; i++){
    if(numArr[i]!=="#"){
      let node = new TreeNode(numArr[i]);
      if (isLeftChild){
        queue[level].left = node;
      } else {
        queue[level].right = node;
      }
      queue.push(node);
    }

    if (!isLeftChild){
      level++;
    }
    isLeftChild = !isLeftChild;
  }
  return root;
}


const input = "{3, 9, 20, #, #, 15, 7}"

const tree = deserialize(input)

console.log(tree)

const output = serialize(tree)

console.log(output)

