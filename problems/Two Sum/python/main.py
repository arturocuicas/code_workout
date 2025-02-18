from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_mapper = {}

        for i, num in enumerate(nums):

            complement = target - num
            if complement in num_mapper:
                return [i, num_mapper[complement]]

            num_mapper[nums[i]] = i

        return []

solution = Solution()

print(solution.two_sum([2, 7, 11, 15], 9)) # [0, 1]
print(solution.two_sum([3, 2, 4], 6)) # [1, 2]
print(solution.two_sum([3, 3], 6)) # [0, 1]