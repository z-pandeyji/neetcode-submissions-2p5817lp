class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      val = {}
      for i in range(len(nums)):
        kval = target - nums[i]
        if kval in val:
          return[val[kval], i]
        val[nums[i]] = i
          

        