class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i, v in enumerate(nums):
            if v in last_seen:
                Oi = last_seen[v]
                if i - Oi <= k:
                    return True
            last_seen[v] = i
            # print(last_seen)
        return False

                



        