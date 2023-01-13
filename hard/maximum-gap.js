// https://leetcode.com/problems/maximum-gap/submissions/876980465/

var maximumGap = function(nums) {
    newresto = 0
    resto = null
    ant = 0
    
    for (item of nums.sort(compareNumbers)) {
        if (resto === null ) {
            resto = 0
            ant = item
        } else {
            resto = item - ant
            ant = item
        }
        resto = Math.abs( resto )
        if (resto > newresto) {
            newresto = resto
            resto = 0
        }
    }
    return newresto
};

function compareNumbers(a, b) {
    return a - b;
  }
console.log(maximumGap([3,6,9,1]))
