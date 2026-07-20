class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        response = count = 0
        for num in nums:
            if num == 0:
                response = max(response, count)
                count = 0
            else:
                count += 1
        
        return max(count, response)