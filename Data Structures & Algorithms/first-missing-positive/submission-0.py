class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            current = nums[i]
            if 1 <= current <= n:
                correct_index = current - 1
                if nums[correct_index] != current:
                    temp = nums[i]
                    nums[i] = nums[correct_index]
                    nums[correct_index] = temp
                    continue
            i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
        