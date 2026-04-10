class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        canditate = None

        for num in nums:
            if count == 0:
                canditate = num
            if num == canditate:
                count += 1
            else: 
                count -= 1
        return canditate

        