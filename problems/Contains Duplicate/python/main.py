from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

solution = Solution()
print(solution.contains_duplicate([1,2,3,1]))
print(solution.contains_duplicate([1,2,3,4]))
print(solution.contains_duplicate([1,1,1,3,3,4,3,2,4,2]))