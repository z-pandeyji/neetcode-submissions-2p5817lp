class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}
        for x in nums:
            prefix = prefix + x
            target = prefix - k
            if target in seen:
                count = count + seen[target]
            if prefix in seen:
                seen[prefix]  = seen[prefix] + 1
            else: 
                seen[prefix] = 1
        return count

        