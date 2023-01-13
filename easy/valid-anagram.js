// https://leetcode.com/problems/valid-anagram/
// codigo pra colar no leet of code ta la embaixo
word1 = "anagram"
word2 = "nagaram"


function isAnagram(w1,w2) {
  an1 = []
  an2 = []

  for (letra of w1) {
    an1.push(letra)
  }
  for (letra of w2) {
    an2.push(letra)
  }

  an1 = an1.sort().toString()
  an2 = an2.sort().toString()

  if (an1 === an2) {
    console.log("É um anagrama")
  } else {
    console.log("Não É um anagrama")

  }

}

isAnagram(word1,word2)


// codigo p colar no site
// /**
//  * @param {string} s
//  * @param {string} t
//  * @return {boolean}
//  */
//  var isAnagram = function(s, t) {
//   an1 = []
//   an2 = []
  
//   for (letra of s) {
//   an1.push(letra)
//   }
//   for (letra of t) {
//       an2.push(letra)
//   }

//   an1 = an1.sort().toString()
//   an2 = an2.sort().toString()

//   if (an1 === an2) {
//       return true
//   } else {
//       return false
//   }
// };