class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}
        for x in nums:
            prefix = prefix + x
            # print(prefix)
            target = prefix - k
            # print(target)
            if target in seen:
                count = count + seen[target]
                # print(count)
            if prefix in seen:
                seen[prefix]  = seen[prefix] + 1
                # print('if')
                # print(seen)
            else: 
                seen[prefix] = 1
                # print('else')
                # print(seen)
        return count

        