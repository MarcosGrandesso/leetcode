// https://leetcode.com/problems/first-missing-positive/submissions/877422551/

var firstMissingPositive = function(nums) {
  contador = 1
  nums.sort(compareNumbers)
  for (i of nums) {
      if ( i < contador) {
        continue
      } else if (i == contador) {
        contador++
      } else if (i != contador) {
        return contador
      } 
    }
    return contador

};


function compareNumbers(a, b) {
  return a - b;
}

console.log(firstMissingPositive([1,2,0]))