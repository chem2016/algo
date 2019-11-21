const doesPathExist = (graph, start, target, visited = {}) => {
  //if there are no nodes connected to the start, return false
  if (!graph[start]) return false
  //start tracking visited nodes --> visited = {start: true}
  visited[start] = true;

  return graph[start].some((vertex) => {
    //if this item in the array is the end of the path, return true
    if (vertex === target) return true;

    //if we have not yet visited this item in the array, keep looking by recursing
    if (!visited[vertex]) {
      return doesPathExist(graph, vertex, target, visited);
      //else, if we have already visited this item in the array, that means we do not want to keep looking infinitely
    } else {
      return false;
    }
  });
}

function dosePathExistBFS(graph, start, target, visited = {}){
  if(!graph[start]) return false;
  let queue = [start]
  while(queue.length){
    let node = queue.shift();
    visited[node] = true;
    console.log('node: ', node)
    let neighbors = graph[node];
    console.log('neighbors: ', neighbors)
    for (let i = 0; i < neighbors.length; i++){
      let vertex = neighbors[i]
      if(vertex === target) return true;
      if(!visited[vertex]){
        queue.push(vertex)
      }
    }
  }
  return false
}

//GRAPH 1
// const graph = {
//   a: ['b'],
//   b: ['c', 'd'],
//   c: ['d'],
//   d: [],
// }
const graph = {
  a: ['b'],
  b: ['c', 'd'],
  d: ['x']
}

//GRAPH 1 OUTPUTS
console.log(doesPathExist(graph, 'a', 'b')) // true
console.log(doesPathExist(graph, 'a', 'e')) // false
console.log(doesPathExist(graph, 'a', 'd')) // true
console.log(doesPathExist(graph, 'a', 'a')) // false

console.log(dosePathExistBFS(graph, 'a', 'b')) // true
console.log(dosePathExistBFS(graph, 'a', 'e')) // false
console.log(dosePathExistBFS(graph, 'a', 'd')) // true
console.log(dosePathExistBFS(graph, 'a', 'a')) // false