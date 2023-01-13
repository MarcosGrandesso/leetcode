// https://leetcode.com/problems/integer-to-roman/submissions/876377996/
var intToRoman = function(num) {

  dict = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
}
  palavra = ''

  for (x of [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]) {

    while (x <= num) {
      palavra += dict[x]
      num -= x
    }
  }
  return palavra
}
console.log(intToRoman())

