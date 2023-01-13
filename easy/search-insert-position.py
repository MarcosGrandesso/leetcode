# https://leetcode.com/problems/search-insert-position/
# codigo comentado abaixo p jogar no leet

def searchInsert(nums: list, target: int) -> int:
        count = 0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
        return sorted(nums).index(target)

print(searchInsert([1,3,5,6], 5))

# jogue esse que tem o argumento self no letcode
# def searchInsert(nums: list, target: int) -> int:
#         count = 0
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#         return sorted(nums).index(target)

# print(searchInsert([1,3,5,6], 5))
