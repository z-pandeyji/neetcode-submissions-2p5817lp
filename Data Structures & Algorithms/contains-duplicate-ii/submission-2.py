class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i, v in enumerate(nums):
            if v in last_seen:
                Old_i = last_seen[v]
                if i - Old_i <= k:
                    return True
            last_seen[v] = i
            # print(last_seen)
        return False

                



        