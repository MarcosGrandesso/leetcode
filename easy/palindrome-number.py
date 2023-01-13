# https://leetcode.com/problems/palindrome-number/

def isPalindrome(self, x: int) -> bool:
    excepts = [11,22,33,44,55,66,77,88,99]

    if (len(str(x)) == 2 and x in excepts) or len(str(x)) == 1:
        return True
    elif x < 100:
        return False
    strng = []
    for i in reversed(str(x)):
        strng.append(i)
    strng = ''.join(strng)
    if x == int(strng):
        return True
print(isPalindrome( 2))

# jogue esse aqui no let code, esse tem o argumento self
# def isPalindrome(self, x: int) -> bool:
#     excepts = [11,22,33,44,55,66,77,88,99]

#     if (len(str(x)) == 2 and x in excepts) or len(str(x)) == 1:
#         return True
#     elif x < 100:
#         return False
#     strng = []
#     for i in reversed(str(x)):
#         strng.append(i)
#     strng = ''.join(strng)
#     if x == int(strng):
#         return True