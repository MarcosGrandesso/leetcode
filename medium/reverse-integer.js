https://leetcode.com/problems/reverse-integer/submissions/877423512/
x= -2147483648

var reverse = function(x) {
  l = []
  is_negative = false
  for (i of String(x)) {
      if (i != '-'){
      l.push(i)
      } else {
        is_negative = true
      }
  }
  l = l.reverse()
  l = l.join("")
  
  if (Number(l) > 2 ** 31 -1) {
      return 0
  }
  if (is_negative) {
    return Number(l) * -1
  }
  return Number(l)

};

console.log( 9646324351 === reverse(x))
//  9646324351