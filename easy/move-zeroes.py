
# https://leetcode.com/problems/move-zeroes/
#  codigo pra jogar no leet code ta no fim do arquivo 
nums = [0,1,0,3,12]

def move_zero_to_end(nums):
  # a = sorted(nums) 
  
  zeros= []
  reverse = []
  for item in nums:
    if item == 0:
        zeros.append(item)
    else:
        reverse.append(item)

  for item in zeros:
    reverse.append(item)

  print(reverse)

  
move_zero_to_end(nums)

#  codigo pra jogar no leet code
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         zeros= []
#         reverse = []
#         for item in nums:
#             if item == 0:
#                 zeros.append(item)
#             else:
#                 reverse.append(item)

#         try:
#             while True:
#                 nums.remove(0)
#         except ValueError:
#             pass

#         for item in zeros:
#             nums.append(item)