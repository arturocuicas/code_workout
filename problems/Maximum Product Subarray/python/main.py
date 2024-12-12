from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = max_product

        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, max_product * current, min_product * current)
            min_product = min(current, max_product * current, min_product * current)

            max_product = temp_max
            result = max(max_product, result)

        return result

solution = Solution()

print(solution.max_product([2, 3, -2, 4])) # 6
print(solution.max_product([-2, 0, -1])) # 0
print(solution.max_product([1, 1, 1, 1])) # 1
print(solution.max_product([5, 5])) # 25