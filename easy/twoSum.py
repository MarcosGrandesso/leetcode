# https://leetcode.com/problems/two-sum/

def twoSum( nums: list, target: int) -> list[int]:
    past = {}

    for index, num in enumerate(nums):
        rest = target - num

        if rest in past:
            return [past[rest], index]

        past[num] = index

print(twoSum([3,2,4],6))