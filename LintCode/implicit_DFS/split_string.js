// public class Solution {
//     /*
//      * @param : a string to be split
//      * @return: all possible split string array
//      */
//     public List<List<String>> splitString(String s) {
//         // write your code here
//         List<List<String>> res = new ArrayList<>();

//         if (s == null) return res;
//         if (s.length() == 0) {
//             res.add(new ArrayList<String>());
//             return res;
//         }

//         dfs(res, new ArrayList<String>(), 0, s);

//         return res;
//     }

//     private void dfs(List<List<String>> res, List<String> cur, int index, String s) {
//         if (index >= s.length()) {
//             res.add(new ArrayList<String>(cur));
//             return;
//         }
        
//         for (int i = index; i < index + 2 && i < s.length(); i++) {
//             String sub = s.substring(index, i + 1);
//             cur.add(sub);
//             dfs(res, cur, i + 1, s);
//             cur.remove(cur.size() - 1);
//         }
        
        
//     }
// }

function splitString(s){
    let res = []
    if (s == null) return res
    if (s.length == 0){
        res.push([])
        return res
    }
    dfs(res, [], 0, s)
    return res
}

function dfs(res, cur, index, s){
    if (index >= s.length){
        res.push(cur)
        return
    }

    for (let i = index; i<index + 2 && i < s.length; i++){
        const sub = s.substring(index, i+1);
        cur.push(sub)
        console.log('cur: ', cur)
        dfs(res, cur, i+1, s);
        cur.pop(cur.length -1)
    }
}

const result = splitString('123')

console.log(result)