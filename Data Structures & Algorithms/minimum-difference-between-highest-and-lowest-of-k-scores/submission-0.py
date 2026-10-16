from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = float("inf")

        for left in range(len(nums) - k + 1):
            right = left + k - 1
            difference = nums[right] - nums[left]
            answer = min(answer, difference)

        return answer