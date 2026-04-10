class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tVal = {}
        for i in range(len(nums)):
            if nums[i] not in tVal:
                tVal[nums[i]] = 1
            else:
                tVal[nums[i]] += 1
        maxV = max(tVal.values())
        for key, value in tVal.items():
            if value == maxV:
                print(key)
                return key

        