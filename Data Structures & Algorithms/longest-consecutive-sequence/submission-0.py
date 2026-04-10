class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            seen.add(x)
        max_len = 0
        for x in nums:
            if (x-1) not in seen:
                current = x
                length = 1
                while(current+1) in seen:
                    current += 1
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len

        